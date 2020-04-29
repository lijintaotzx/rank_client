# coding=utf-8
from rest_framework import serializers

from ranking.models import RankingList


class RankingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = RankingList
        fields = '__all__'


class ClientNameSerializer(serializers.Serializer):
    my_client_name = serializers.CharField(max_length=64)
    start = serializers.IntegerField(default=None)
    end = serializers.IntegerField(default=None)

    def validate_my_client_name(self, data):
        rank_filter = RankingList.objects.filter(client_name=data).count()
        if rank_filter == 0:
            raise serializers.ValidationError('客户端名称有误！')
        return data
