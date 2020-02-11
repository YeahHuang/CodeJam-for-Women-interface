from bisect import bisect_left, bisect_right, insort_left,  insort_right
from string import ascii_lowercase
from heapq import heappush, heappop, heapify
from collections import Counter, defaultdict
from itertools import product
"""
K ingredients 每个appear 1次
distance to bun
optimal distance-to-bun value Di

minimize error value: （实际值 - Di）平方和

因为范围限制 可以直接sort
按照一前一后的顺序摆 即可？ 

10:12 AC 12min
"""
T = int(input())

for it in range(T):
    k = int(input())
    p = list(map(int, input().split()))
    p.sort()
    ans = 0
    for i in range(k):
        ans += (p[i] - (i//2))**2
    print("Case #%d: %d"%(it+1, ans))