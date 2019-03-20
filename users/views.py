from django.shortcuts import render,HttpResponse
from users.models import UserInfo
import time
from django.views.decorators.cache import cache_page
from django.db.models.signals import pre_init,post_save

from django.dispatch import receiver
from django.core.signals import request_finished
# Create your views here.


from django.core.cache import cache
from django.http import HttpRequest
from django.utils.cache import get_cache_key


import django.dispatch
pizza_done = django.dispatch.Signal(providing_args=["toppings", 'url'])

"""
通过信号量机制清除缓存

"""

def req_fin_call(**kwargs):
    print(kwargs)
    request = kwargs['toppings']
    url = kwargs['url']
    request.path = url
    key = get_cache_key(request)

    if cache.has_key(key):
        cache.delete(key)
    print("request_finished")

pizza_done.connect(req_fin_call)


@cache_page(15)
def index(request):
    user_list = UserInfo.objects.all()

    ctime =time.time()
    url = request.build_absolute_uri()


    pizza_done.send(sender='pig',toppings=request,url=url)

    return render(request,'index.html',{"user_list":user_list,"ctime":ctime})



