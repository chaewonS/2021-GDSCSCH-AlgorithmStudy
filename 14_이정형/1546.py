# -*- coding: utf-8 -*-
import sys

n = int(input())
exam_list = list(map(float, sys.stdin.readline().split()))
max_score = max(exam_list)

fake_score_list = []
for i in exam_list:
    fake_score_list.append(i / max_score * 100)
exam_evg = sum(fake_score_list) / n
print(exam_evg)
