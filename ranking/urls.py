# coding=utf-8
from django.conf.urls import url

from ranking.views import RankScoreView

urlpatterns = [
    url(r'^client_score/$', RankScoreView.as_view()),
]
