from bisect import bisect_left, bisect_right, insort_left,  insort_right
from string import ascii_lowercase
from heapq import heappush, heappop, heapify
from collections import Counter, defaultdict
from itertools import product

"""
experience level: Ei>=0 

direct manager: E(manager) > E(employee) 且不能是CEO
Ei 只能做<=E个employee的direct manager 且它不具备传递性
Ei递增

直觉： 相邻层的做相邻层的manager

10:21 AC 10:12-10:21
"""

T = int(input())

for it in range(T):
    l = int(input())
    remain = 0 
    for i in range(l):
        n, e = map(int, input().split())
        if n * e < remain:
            remain = remain - n*e + n
        else:
            remain = 0 + n
    ans = max(remain, e + 1)
    print("Case #%d: %d"%(it+1, ans))