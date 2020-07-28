# from django.db import models
#
# # Create your models here.
#
#
# class Url(models.Model):
#     url = models.CharField(max_length=200)

from django.db import models
from hashlib import md5
import time
import string
from random import randint

base_list = string.ascii_letters + string.digits


def encoder(num):
    result = []
    while num:
        result.append(base_list[num % 62])
        num //= 62
    return "".join(reversed(result))


class Link(models.Model):
    origin_url = models.URLField("Url", help_text='your shortended URL will be computed')
    short_url = models.URLField(unique=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='created')

    def save(self, *args, **kwargs):
        if not self.id:
            millis = int(round(time.time() * 1000))
            encoded_url = md5(self.origin_url.encode()).hexdigest()[:10]
            url_Num = 0
            ran_num = 0

            #generate encoded url to integer
            for i in encoded_url:
                url_Num += ord(i)

            #generate random integers
            for _ in range(100):
                ran_num = randint(0, 100)

            self.short_url = encoder(millis) + encoder(url_Num) + encoder(ran_num)
        return super().save(*args, **kwargs)
