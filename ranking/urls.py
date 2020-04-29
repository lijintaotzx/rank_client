# coding=utf-8
from django.conf.urls import url

from ranking.views import (
    RankScoreView,
    RankingListView,
)

urlpatterns = [
    url(r'^client_score/$', RankScoreView.as_view()),
    url(r'^ranking_list/$', RankingListView.as_view()),
]
