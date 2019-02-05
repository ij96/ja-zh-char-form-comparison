#!/usr/bin/python3.5

# check and locate if an input text file contains Simplified Chinese characters whose
# corresponding Japanese characters forms are different.
# this can be useful to check if a file that supposedly contain Japanese text was
# taken from Baidu, as posts on Baidu get converted to simplified Chinese
# (specifically the GB2312-80 set).

import sys
import csv

detect_ja_new = True  # shinjitai
detect_ja_old = False # kyuujitai
detect_zht = False

# construct diff_dict
diff_dict = {}

# shinjitai (new Japanese character forms)
if detect_ja_new:
    with open('../dict/jouyoukanji_shinjitai_ja-zhs_diff.csv', 'r') as diff_file:
      diff_reader = csv.reader(diff_file, delimiter=',')
      diff_dict.update({row[1]:row[0] for row in diff_reader})

# traditional Chinese
if detect_ja_old:
    with open('../dict/GB2312-80_zhs-zht_diff.csv', 'r') as diff_file:
      diff_reader = csv.reader(diff_file, delimiter=',')
      diff_dict.update({row[0]:row[1] for row in diff_reader})

# kyuujitai (old Japanese character forms)
if detect_zht:
    with open('../dict/jouyoukanji_kyuujitai_ja-zhs_diff.csv', 'r') as diff_file:
      diff_reader = csv.reader(diff_file, delimiter=',')
      diff_dict.update({row[1]:row[0] for row in diff_reader})

# open the file to be checked, and check for each char if it is present in diff_dict
line_counter = 0
col_counter = 0
with open(sys.argv[1], 'r') as file:
    for line in file:
        line_counter += 1
        col_counter = 0
        for col in line:
            col_counter += 1
            if col in diff_dict.keys():
                print('line {} column {}: {}, {}'.format(line_counter, col_counter, col, diff_dict[col]))
