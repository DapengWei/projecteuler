#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_sunday(x_days):
        if x_days % 7 == 6:
            return 1
        else:
            return 0


def main():
    days = 365 % 7
    sundays = 0
    for year in xrange(1901, 2001):
        if (year % 400 == 0) or ((year % 100 != 0 and year % 4 == 0)):
            days_list = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            days_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for month_days in days_list:
            sundays = sundays + is_sunday(days)
            days = (days + month_days) % 7
    print sundays

if __name__ == '__main__':
    main()
