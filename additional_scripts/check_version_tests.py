# coding=utf-8
import unittest

from scripts.check_version_script import check_version


class TestCheckVersion(unittest.TestCase):
    def setUp(self):
        self.one_result_list = [
            ('1.2.4', '1.2.3'),
            ('1.2.3', '1.1'),
            ('1.23.3', '1.0.34'),
            ('1.0.1', '1'),
        ]
        self.minus_one_result_list = [
            ('0.1', '1.1'),
            ('7.5.2.4', '7.5.3'),
            ('1.2.3', '1.2.4'),
            ('1', '1.0.1'),
        ]
        self.zero_result_list = [
            ('1.01', '1.001'),
            ('1.0', '1.0.0'),
        ]

    # 测试所有结果为1的情况
    def test_result_one(self):
        for v1, v2 in self.one_result_list:
            self.assertEqual(check_version(v1, v2), 1)

    # 测试所有结果为-1的情况
    def test_result_minus_one(self):
        for v1, v2 in self.minus_one_result_list:
            self.assertEqual(check_version(v1, v2), -1)

    # 测试所有结果为0的情况
    def test_result_zero(self):
        for v1, v2 in self.zero_result_list:
            self.assertEqual(check_version(v1, v2), 0)
