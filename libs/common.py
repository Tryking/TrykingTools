#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging
import random
import logging.handlers
import os
import inspect
import re
import time


def init_log(console_level, file_level, logfile):
    formatter = logging.Formatter('%(name)-12s %(asctime)s %(levelname)-8s %(message)s')
    logging.getLogger().setLevel(0)
    console_log = logging.StreamHandler()
    console_log.setLevel(console_level)
    console_log.setFormatter(formatter)
    file_log = logging.handlers.RotatingFileHandler(logfile, maxBytes=1024 * 1024, backupCount=10,
                                                    encoding='UTF-8')
    file_log.setLevel(file_level)
    file_log.setFormatter(formatter)
    logging.getLogger().addHandler(file_log)
    logging.getLogger().addHandler(console_log)


def write_file_log(msg, __module='', level='error'):
    filename = os.path.split(__file__)[1]
    if level == 'debug':
        logging.getLogger().debug('File:' + filename + ', ' + __module + ': ' + msg)
    elif level == 'warning':
        logging.getLogger().warning('File:' + filename + ', ' + __module + ': ' + msg)
    else:
        logging.getLogger().error('File:' + filename + ', ' + __module + ': ' + msg)


def get_random_str(str_len):
    content = 'abcdefghijklmnopqrstuvwxyz1234567890'
    result = random.choices(content, str_len)
    return ''.join(result)


def get_current_func_name():
    return inspect.stack()[1][3]


def get_current_time_str():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


def get_current_date_str():
    return time.strftime("%m.%d", time.localtime())


# 获取前几天的月份字符串
def get_before_month_str(before_day=None):
    # 默认获取昨天的
    if before_day is None:
        before_day = 1
    return time.strftime("%m", time.localtime(time.time() - 3600 * 24 * before_day))


# 获取今日的月份字符串
def get_current_month_str(before_day=None):
    return time.strftime("%m", time.localtime())


# 获取今日的日期字符串
def get_current_day_str(before_day=None):
    return time.strftime("%d", time.localtime())


# 获取前几天的日期字符串(包含年)
def get_before_date(before_day=None):
    # 默认获取昨天的
    if before_day is None:
        before_day = 1
    return time.strftime("%Y-%m-%d", time.localtime(time.time() - 3600 * 24 * before_day))


# 获取前几天的日期字符串(不包含年)
def get_before_date_str(before_day=None):
    # 默认获取昨天的
    if before_day is None:
        before_day = 1
    return time.strftime("%m.%d", time.localtime(time.time() - 3600 * 24 * before_day))


def time_to_format(timestamp):
    try:
        time_format = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(timestamp))
        return time_format
    except Exception as e:
        raise e


def get_time_str(timestamp):
    try:
        time_format = time.strftime("%H%M%S", time.localtime(timestamp))
        return time_format
    except Exception as e:
        raise e


def format_to_time(time_format):
    try:
        time_array = time.strptime(time_format, "%Y-%m-%d %H:%M:%S")
        timestamp = time.mktime(time_array)
        return timestamp
    except Exception as e:
        raise e


def get_legal_file_name(original):
    try:
        return re.sub('[\/:*?"<>|]', '-', original)  # 去掉非法字符
    except Exception as e:
        raise e
