from bisect import bisect_left, bisect_right, insort_left,  insort_right
from string import ascii_lowercase
from heapq import heappush, heappop, heapify
from collections import Counter, defaultdict
from itertools import product
import random

T = int(input())

#UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
UPPER = "ABCD"
for it in range(T):
    n = int(input())
    pwds = list(input().split())
    p = pwds[0]
    ans = UPPER
    for p in pwds:
        if len(p) == 1:
            ans = "IMPOSSIBLE"
            break
    if ans == UPPER:
        ans = "IMPOSSIBLE"
        for cnt in range(100):
            tmp = list(UPPER)
            random.shuffle(tmp)
            s = "".join(tmp)
            print(s)
            flag = True
            for p in pwds:
                if s.find(p) != -1:
                    flag = False
                    break
            if flag:
                ans = s
                break
        
    print("Case #%d: %s"%(it+1, ans))