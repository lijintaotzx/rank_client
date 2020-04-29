from django.db import models


# Create your models here.

class ClientScore(models.Model):
    client_name = models.CharField(verbose_name='客户端名称', max_length=64)
    score = models.IntegerField(verbose_name='分值')
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    def __str__(self):
        return '{}:{}'.format(self.client_name, self.score)

    class Meta:
        verbose_name = '客户端分值表'
        verbose_name_plural = '客户端分值表'


class RankingList(models.Model):
    client_name = models.CharField(verbose_name='客户端名称', max_length=64)
    score = models.IntegerField(verbose_name='分值')

    class Meta:
        ordering = ['score']
        verbose_name = '客户端排名表'
        verbose_name_plural = '客户端排名表'
