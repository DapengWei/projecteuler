#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    step = [[1 for i in range(21)] for j in range(21)]
    for i in xrange(1, 21):
        for j in xrange(1, 21):
            step[i][j] = step[i-1][j] + step[i][j-1]
    print step[20][20]

if __name__ == '__main__':
    main()
