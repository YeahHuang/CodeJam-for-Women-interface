"""
一次打一个字母 
每个event打印0..次

>=0个数量的电脑
不一定打印相同次

保证有解
两个stack pop 
其实只要计数即可 遇到o -1 O 先减I 
"""
from bisect import bisect_left, bisect_right, insort_left,  insort_right
from string import ascii_lowercase
from heapq import heappush, heappop, heapify
from collections import Counter, defaultdict
from itertools import product
from random import randint
from operator import add
from re import split, sub

T = int(input())

for it in range(T):
    s = input()
    ans = 0
    cnt_i, cnt_I = 0, 0
    for c in s:
        if c=="i":
            cnt_i += 1
        elif c=="I":
            cnt_I += 1
        elif c=="o":
            if cnt_i > 0:
                cnt_i -= 1
            else:
                cnt_I -= 1
        else: #c=="O"
            if cnt_I >0:
                cnt_I -= 1
                ans += 1
            else:
                cnt_i -= 1

    print("Case #%d: %d"%(it+1, ans))