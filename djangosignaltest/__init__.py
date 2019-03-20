from django.db.models.signals import pre_init,post_save

from django.dispatch import receiver
from django.core.signals import request_finished



from django.core.cache import cache
from django.http import HttpRequest
from django.utils.cache import get_cache_key


@receiver(post_save)
def callback(sender,**kwargs):

    """
    相关操作
    :param sender:
    :param kwargs:
    :return:
    """
    print("postsave")


@receiver(request_finished)
def req_fin_call(**kwargs):
    """
    相关操作
    :param kwargs:
    :return:
    """

    print("自动触发")

