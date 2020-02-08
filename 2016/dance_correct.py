from bisect import bisect_left, bisect_right, insort_left,  insort_right
from string import ascii_lowercase
from heapq import heappush, heappop, heapify
from collections import Counter, defaultdict
from itertools import product

"""
小数据集 n<=10 必然模拟
大数据集 n<=1e8 找规律咯～
"""


T = int(input())

for it in range(T):
    d, k, n  = map(int, input().split())
    t = [i+1 for i in range(d)]
    for j in range(n):
        if t[0] & 1:
            for i in range(d//2):
                t[i*2], t[i*2+1] = t[i*2+1], t[i*2]
        else:
            for i in range(d//2):
                t[i*2-1], t[i*2] = t[i*2], t[i*2-1]
        #print(t)
    idx = t.index(k)
    print("Case #%d: %d %d"%(it+1, t[(idx+1)%d], t[idx-1]))