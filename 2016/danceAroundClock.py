from bisect import bisect_left, bisect_right, insort_left,  insort_right
from string import ascii_lowercase
from heapq import heappush, heappop, heapify
from collections import Counter, defaultdict
from itertools import product

"""
小数据集 n<=10 必然模拟
大数据集 n<=1e8 找规律咯～
    D is even 每次奇偶对调 
    所以总是左边转一次 右边转一次的
"""


T = int(input())

for it in range(T):
    d, k, n  = map(int, input().split())
    t = [i+1 for i in range(d)]
    idx = k-1
    f = [(t[(idx+1)%d], t[idx-1])]
    y, z = 0, 0 
    for j in range(n):
        if t[0] & 1:
            for i in range(d//2):
                t[i*2], t[i*2+1] = t[i*2+1], t[i*2]
        else:
            for i in range(d//2):
                t[i*2-1], t[i*2] = t[i*2], t[i*2-1]
        #print(t)
        if t[idx-1] == k:
            idx = (idx + d - 1) %d
        else:
            idx = (idx+1)%d
        #print(t)
        #if t[(idx+1)%d] == f[0][0] and t[idx-1] == f[0][1]:
        if (t[(idx+1)%d], t[idx-1]) in f:
            start_idx = f.index((t[(idx+1)%d], t[idx-1]))
            cycle = j - start_idx + 1
            y, z = f[(n-start_idx)%cycle+start_idx][0], f[(n-start_idx)%cycle+start_idx][1]
            """
            print(start_idx)
            print(cycle)
            print(f)
            """
            break
        else:
            f.append((t[(idx+1)%d], t[idx-1]))
    #print("Case #%d: %d %d"%(it+1, t[idx+1], t[idx-1])) 忘记%d了 RE一次
    if y == 0:
        #print(idx)
        idx = t.index(k)
        y, z = t[(idx+1)%d], t[idx-1]
    print("Case #%d: %d %d"%(it+1, y, z))