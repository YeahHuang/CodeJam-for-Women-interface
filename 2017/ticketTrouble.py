from bisect import bisect_left, bisect_right, insort_left,  insort_right
from string import ascii_lowercase
from heapq import heappush, heappop, heapify
from collections import Counter, defaultdict
from itertools import product

"""
F friends
S rows and S columns 

(2,1) row 2 col 1
最多多少人 row 相等？ 不一定要连续

1. 每一个row 一个set
2. set数量 max

6min AC

"""
T = int(input())

for it in range(T):
    f, s = map(int, input().split())
    seats = [set() for _ in range(s+1)]
    for i in range(f):
        a, b = map(int, input().split())
        seats[a].add(b)
        seats[b].add(a)
    ans = max([len(seats[i]) for i in range(s+1)])
    print("Case #%d: %d"%(it+1, ans))