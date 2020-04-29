from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status

from ranking.models import ClientScore
from ranking.serializers.client_score_serializer import ClientScoreSerializer


class RankScoreView(CreateAPIView):
    queryset = ClientScore.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = ClientScoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': '创建成功！'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
