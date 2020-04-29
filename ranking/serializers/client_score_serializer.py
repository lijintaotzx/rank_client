# coding=utf-8
from rest_framework import serializers

from ranking.models import ClientScore


class ClientScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientScore
        fields = '__all__'

    def validate_score(self, data):
        if data < 0 or data > 10000000:
            raise serializers.ValidationError('客户端分值范围：0-10000000！')
        return data
