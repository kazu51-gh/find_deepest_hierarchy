#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'TATSUMI Kazuto'
__version__ = '1.0.0'
__date__ = '2022/12/01'

import os
import sys

def main():
    path = os.getcwd()  # 現在のディレクトリを取得
    deepest_dir = ''    # 1番深いディレクトリ階層を保持
    deepest_count = 0   # 1番深いディレクトリの階層数を保持

    for dirpath, dirnames, filenames in os.walk(path):
        number_of_hierarchy = get_the_number_of_hierarchy(dirpath)
        deepest_dir, deepest_count = update_path_and_hierarchy(deepest_count, deepest_dir, number_of_hierarchy, dirpath)
    
    print(f'最深ディレクトリのパス : {deepest_dir}')
    print(f'最深ディレクトリの階層数は{deepest_count}です.')

    return 0

# 取得したディレクトリの階層数を取得する
def get_the_number_of_hierarchy(current_dir):
    list = current_dir.split('/')
    return len(list)

# 1番深いディレクトリのパスと階層数を更新する
def update_path_and_hierarchy(deepest_count, deepest_dir, number_of_hierarchy, current_dir):
    if deepest_count < number_of_hierarchy:
        deepest_count = number_of_hierarchy
        deepest_dir = current_dir
    return deepest_dir, deepest_count



if __name__ == '__main__':
    sys.exit(main())