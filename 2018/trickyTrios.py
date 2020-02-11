from bisect import bisect_left, bisect_right, insort_left,  insort_right
from string import ascii_lowercase
from heapq import heappush, heappop, heapify
from collections import Counter, defaultdict
from itertools import product
"""
3N 1...N的卡片各3张 

翻2张 不同skip 
        else 翻第3张 相同则trio
        
翻过的牌记得在哪儿 

概率题

首先是可以递推？ 因为每一个f[n] 除去后就剩下几个了 当然有已知位置


小数据集也可以手算


11:18-
1 


"""


T = int(input())

for it in range(T):
    l, r = map(int, input().split())
    p = list(map(int, input().split()))
    ans = 0
    print("Case #%d: %d"%(it+1, ans))