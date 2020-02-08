from bisect import bisect_left, bisect_right, insort_left,  insort_right
from string import ascii_lowercase
from heapq import heappush, heappop, heapify
from collections import Counter, defaultdict
from itertools import product

"""
c = v = 1 多的时候也是直接乘即可



"""
T = int(input())

MOD = 1e9 + 7

for it in range(T):
    c, v, l = map(int, input().split())
    f = [[v,c] for _ in range(l)]
    for i in range(1,l):
        #python的乘法大的也是有边界的 因为没有MOD WA一次 
        f[i][0] = (f[i-1][0] + f[i-1][1])*v % MOD  #is vowel 
        f[i][1] = f[i-1][0]*c % MOD #is consonants
    ans = f[-1][0] % MOD


    print("Case #%d: %d"%(it+1, ans))





