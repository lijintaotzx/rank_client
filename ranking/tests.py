# coding=utf-8
import random

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ranking.models import ClientScore, RankingList


class RankScoreViewTest(APITestCase):
    def setUp(self):
        self.url = reverse('client_score')

        self.correct_parameter_list = [
            {'client_name': '客户端{}'.format(client_id), 'score': random.randint(1, 10000000)}
            for client_id in range(1, 11)
        ]
        self.correct_parameter_list.extend(
            [
                {'client_name': '客户端1', 'score': 11},
                {'client_name': '客户端2', 'score': 12},
                {'client_name': '客户端3', 'score': 13},
                {'client_name': '客户端4', 'score': 14},
                {'client_name': '客户端5', 'score': 15},
            ]
        )

        self.error_parameter_list = [
            {'client_name': '客户端1', 'score': -1},
            {'client_name': '客户端1', 'score': 10000001}
        ]

    # 测试正确参数的API调用结果，以及 ClientScore表 和 RankingList表
    def test_create_client_score_with_correct_parameter(self):
        for data in self.correct_parameter_list:
            # 创建所有正确参数的客户端分值，并验证接口状态
            response = self.client.post(self.url, data)
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # 检查ClientScore数据
        client_score_count = ClientScore.objects.count()
        self.assertEqual(client_score_count, 15)

        # 检查RankingList数据
        ranking_list_count = RankingList.objects.count()
        self.assertEqual(ranking_list_count, 10)

        # 抽样检查排名表中的数据是不是最新的
        client_1_ranking_score = RankingList.objects.get(client_name='客户端1').score
        client_3_ranking_score = RankingList.objects.get(client_name='客户端3').score
        client_4_ranking_score = RankingList.objects.get(client_name='客户端4').score
        self.assertEqual(client_1_ranking_score, 11)
        self.assertEqual(client_3_ranking_score, 13)
        self.assertEqual(client_4_ranking_score, 14)

    # 测试错误参数的API调用结果，以及ClientScore表 和 RankingList表
    def test_create_client_score_with_error_parameter(self):
        for data in self.error_parameter_list:
            # 创建所有错误参数的客户端分值，并验证接口状态
            response = self.client.post(self.url, data)
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # 检查ClientScore数据
        client_score_count = ClientScore.objects.count()
        self.assertEqual(client_score_count, 0)

        # 检查RankingList数据
        ranking_list_count = RankingList.objects.count()
        self.assertEqual(ranking_list_count, 0)


class RankingListViewTest(APITestCase):
    def setUp(self):
        self.url = reverse('ranking_list')

        self.db_init_data = [
            {'client_name': '客户端3', 'score': 30},
            {'client_name': '客户端2', 'score': 20},
            {'client_name': '客户端1', 'score': 10},
            {'client_name': '客户端4', 'score': 40},
            {'client_name': '客户端5', 'score': 50},
            {'client_name': '客户端6', 'score': 20},
            {'client_name': '客户端8', 'score': 30},
            {'client_name': '客户端7', 'score': 80},
            {'client_name': '客户端10', 'score': 90},
            {'client_name': '客户端9', 'score': 100},
        ]
        for data in self.db_init_data:
            RankingList.objects.create(**data)

        self.correct_my_client_name = '客户端1'
        self.error_my_client_name = '这是一个错误的客户端名称！'
        self.start_parameter = 3
        self.end_parameter = 6
        self.error_start_parameter = '这是一个错误的开始时间'
        self.error_end_parameter = '这是一个错误的结束时间'

    # 测试不加时间间隔参数的调用结果
    def test_get_ranking_list_without_interval(self):
        response = self.client.get(self.url, {'my_client_name': self.correct_my_client_name})

        # 检查接口状态码
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # 检查接口数据列表总条数
        self.assertEqual(len(response.data), len(self.db_init_data) + 1)

        # 检查接口最后一项是不是调用客户端的分值
        self.assertEqual(response.data[-1]['client_name'], self.correct_my_client_name)
        self.assertEqual(response.data[-1]['score'], 10)

        # 抽样检查接口结果排序是否正确
        self.assertEqual(response.data[3]['score'], 50)
        self.assertEqual(response.data[6]['client_name'], '客户端8')
        self.assertEqual(response.data[9]['score'], 10)

    # 测试添加时间间隔的调用结果
    def test_get_ranking_list_with_interval(self):
        response = self.client.get(self.url, {
            'my_client_name': self.correct_my_client_name,
            'start': self.start_parameter,
            'end': self.end_parameter,
        })

        # 检查接口状态码
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # 检查接口数据列表总条数
        self.assertEqual(len(response.data), 5)

        # 检查接口最后一项是不是调用客户端的分值
        self.assertEqual(response.data[-1]['client_name'], self.correct_my_client_name)
        self.assertEqual(response.data[-1]['score'], 10)

        # 抽样检查接口结果排序是否正确
        self.assertEqual(response.data[0]['score'], 80)
        self.assertEqual(response.data[1]['client_name'], '客户端5')
        self.assertEqual(response.data[2]['score'], 40)

    # 测试错误参数的调用结果
    def test_get_ranking_list_with_error_parameter(self):
        response = self.client.get(self.url, {'my_client_name': self.error_my_client_name})

        # 检查接口返回状态码
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # 测试错误的时间间隔参数调用结果
    def test_get_ranking_list_with_error_interval(self):
        response = self.client.get(self.url, {
            'my_client_name': self.correct_my_client_name,
            'start': self.error_start_parameter,
            'end': self.error_end_parameter,
        })

        # 检查接口返回状态码
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
