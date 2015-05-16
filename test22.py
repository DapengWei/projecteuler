#!/usr/bin/env python
# -*- coding: utf-8 -*-


def read_name(file_name):
        list_name = []
        with file(file_name, "r") as name_file:
                name_read = name_file.read()
                for name_item in name_read.strip("\n").split(","):
                        list_name.append(name_item.strip('"').upper())
        list_name.sort()
        return list_name


def main():
        name_list = read_name("test22_names.txt")
        name_scores_all = 0
        name_order = 1
        for name_str in name_list:
                name_scores = 0
                for name_letter in name_str.lower():
                        name_scores = name_scores + ((ord(name_letter) - 96) * name_order)
                name_scores_all = name_scores_all + name_scores
                print name_str,name_order,name_scores
                name_order = name_order + 1
        print name_scores_all

if __name__ == '__main__':
    main()
