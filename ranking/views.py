# Create your views here.
from django.forms.models import model_to_dict
from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
)
from rest_framework.response import Response

from ranking.models import (
    ClientScore,
    RankingList,
)
from ranking.serializers.client_score_serializer import ClientScoreSerializer
from ranking.serializers.ranking_list_serializer import (
    RankingListSerializer,
    ClientNameSerializer,
)


class RankScoreView(CreateAPIView):
    queryset = ClientScore.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = ClientScoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': '创建成功！'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RankingListView(ListAPIView):
    queryset = RankingList.objects.all()
    serializer_class = RankingListSerializer

    def insert_my_score(self, s_data, my_client_name):
        my_score = RankingList.objects.get(client_name=my_client_name)
        s_data.data.append(
            model_to_dict(my_score)
        )
        return s_data

    def list(self, request, *args, **kwargs):
        s = ClientNameSerializer(data=request.query_params)
        if s.is_valid():
            serializer_data = super(ListAPIView, self).list(request, *args, **kwargs)
            return self.insert_my_score(serializer_data, s.data['my_client_name'])
        return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)
