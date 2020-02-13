from bisect import bisect_left, bisect_right, insort_left,  insort_right
from string import ascii_lowercase
from heapq import heappush, heappop, heapify
from collections import Counter, defaultdict
from itertools import product
"""
概率题 
猜测两头扔 结果过了
12min看题 
一共18minAC
"""
T = int(input())

for it in range(T):
    n = int(input())
    p = list(map(float, input().split()))
    p.sort()
    #print(p)
    ans = 1.0
    for l in range(n):
        ans *= 1 - p[l] * p[2*n-1-l]
        #print(l, p[l], p[2*n-1-l],ans)

    print("Case #%d: %f"%(it+1, ans))