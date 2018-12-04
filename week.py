#!/usr/bin/python3 coding=utf-8


def is_leap_year(year):
    """
    判断是不是润年
    :param year: 当前年的4为数字，例如2018
    :return: 是闰年返回 true 否则返回 false
    """
    return (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0)


def get_month_days(month, year, day):
    """
    获取这一年的月份经历了多少天，如果是闰年还没过润的的那一天默认减一天
    :param month: 月份
    :param year:  年份
    :param day:  日期
    :return:
    """
    months = {
        0: 0,
        1: 31,
        2: 59,
        3: 90,
        4: 120,
        5: 151,
        6: 181,
        7: 212,
        8: 243,
        9: 273,
        10: 304,
        11: 334
    }
    if is_leap_year(year) and month in [0, 1] and day < 29:
        return months[month] - 1
    else:
        return months[month]


def get_year_day(year):
    """
    计算距离2000，年份经历了多少天，闰年默认+1
    :param year: 年份
    :return:
    """
    # 距离2000年，经历了多少闰年
    times = (year - 2000) // 4
    # 距离整年经历了多少天
    return (year - 2000) * 365 + times + 1


def print_week(year, month, day):
    """
    计算给的日期是周几
    :param year: 年份
    :param month: 月份
    :param day:  日
    :return:
    """
    # 距离2000年1月1日（周六）多少天
    days = get_year_day(year) + get_month_days(month - 1, year, day) + day
    weeks = {
        0: "星期五",
        1: "星期六",
        2: "星期天",
        3: "星期一",
        4: "星期二",
        5: "星期三",
        6: "星期四"
    }
    print(data + "->" + weeks[days % 7])


if __name__ == "__main__":
    index = 0
    while index < 10:
        try:
            data = input("请输入一个大于20000101的日期:")
            year1 = int(data[0:4])
            month1 = int(data[4:6])
            day1 = int(data[6:8])
            print_week(year1, month1, day1)
            ++index
        except ValueError:
            print("输入年份有误")
