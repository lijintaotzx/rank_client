# coding=utf-8

def format_split_version(v1_list, v2_list):
    """
    统一版本列表长度
    :param v1_list: ['7', '5', '2', '4']
    :param v2_list: ['7', '5', '3']
    :return: (['7', '5', '2', '4'], ['7', '5', '3', 0])
    """
    lenth_diff = len(v1_list) - len(v2_list)
    if lenth_diff > 0:
        for x in range(lenth_diff):
            v2_list.append('0')
        return

    if lenth_diff < 0:
        for x in range(abs(lenth_diff)):
            v1_list.append('0')
        return

    return


def ignore_zero(v1_value, v2_value):
    """
    忽略前置0, 后补缺少0
    :param v1_value: 0001000
    :param v2_value: 12
    :return: ('1000', '1200')
    """
    v1_value = str(int(v1_value))
    v2_value = str(int(v2_value))

    lenth_diff = len(v1_value) - len(v2_value)
    if lenth_diff > 0:
        v2_value += '0' * lenth_diff
    if lenth_diff < 0:
        v1_value += '0' * abs(lenth_diff)

    return v1_value, v2_value


def check_version(v1, v2):
    """
    比较v1与v2的版本号大小
    :param v1: version_1
    :param v2: version_2
    :return: version_1 > version_2: 1,  version_1 < version_2 : -1, 其余情况：0
    """
    v1_list = v1.split('.')
    v2_list = v2.split('.')

    if not len(v1_list) == len(v2_list):
        format_split_version(v1_list, v2_list)

    for index in range(len(v1_list)):
        v1_value, v2_value = ignore_zero(v1_list[index], v2_list[index])

        if v1_value > v2_value:
            return 1
        if v1_value < v2_value:
            return -1

    return 0
