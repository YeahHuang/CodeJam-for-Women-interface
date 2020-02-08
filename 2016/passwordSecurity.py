from bisect import bisect_left, bisect_right, insort_left,  insort_right
from string import ascii_lowercase
from heapq import heappush, heappop, heapify
from collections import Counter, defaultdict
from itertools import product

T = int(input())

UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for it in range(T):
    n = int(input())
    pwds = list(input().split())
    p = pwds[0]
    if len(p) == 1:
        ans = "IMPOSSIBLE"
    else:
        if Counter(p).most_common()[0][1] > 1:
            ans = UPPER
        elif len(p) == 26:
            ans = p[1] + p[0] + p[2:]
        else:
            ans = p[1] + p[0] + p[2:]
            for c in UPPER:
                if c not in p:
                    ans += c
    print("Case #%d: %s"%(it+1, ans))