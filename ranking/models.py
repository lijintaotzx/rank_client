from django.db import models

# Create your models here.
from django.db.models.signals import post_save


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


# 信号更新排行榜数据
def update_rank_list(sender, instance, created, **kwargs):
    if created:
        filter_count = RankingList.objects.filter(client_name=instance.client_name).count()
        if filter_count == 0:
            RankingList.objects.create(client_name=instance.client_name, score=instance.score)
        elif filter_count == 1:
            ins = RankingList.objects.get(client_name=instance.client_name)
            ins.score = instance.score
            ins.save()
        else:
            # TODO 排行榜有多余数据，打印入日志文件，及时处理
            pass


post_save.connect(update_rank_list, ClientScore)
