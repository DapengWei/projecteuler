#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import ceil


def divisors_sum(num):
        sum_num = 0
        for i in xrange(1, int(ceil(num/2)+1)):
                if num % i == 0:
                        sum_num = sum_num + i
        return sum_num


def main():
        ami_sum = []
        for i in xrange(1, 10001):
                ami_num = divisors_sum(i)
                if i == divisors_sum(ami_num) and i != ami_num:
                        if i not in ami_sum:
                                ami_sum.append(i)
                        if ami_num not in ami_sum:
                                ami_sum.append(ami_num)
        print sum(ami_sum)

if __name__ == '__main__':
    main()
