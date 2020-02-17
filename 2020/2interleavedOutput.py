
from bisect import bisect_left, bisect_right, insort_left,  insort_right
from string import ascii_lowercase
from heapq import heappush, heappop, heapify
from collections import Counter, defaultdict
from itertools import product
from random import randint
from operator import add
from re import split, sub

"""
一次打一个字母 
每个event打印0..次

每一个机器只有1个 不一定打印数量相同


保证有解

其实只要计数即可 遇到o -1 O 先减I 

小数据集： 8
两个stack pop 
猜想： 若相邻 则少放一个 不行 无法避免冲突

3:25 - 3:42
"""

global ans

def dfs(hh, hl, lh, ll , i, s, cur):
    global ans
    if i == len(s):
        ans = max(ans, cur)
        return
    if s[i]=="I":
        if hh == 0:
            dfs(hh+1, hl, lh, ll, i+1, s, cur)
        if hl == 0:
            dfs(hh, hl+1, lh, ll, i+1, s, cur)
    elif s[i]=="i":
        if lh==0:
            dfs(hh, hl, lh+1, ll, i+1, s, cur)
        if ll == 0:
            dfs(hh, hl, lh, ll+1, i+1, s, cur)
    elif s[i]=="O":
        if hh == 1:
            #print(hh, hl, lh, ll, i+1, s, cur)
            dfs(hh-1, hl, lh, ll, i+1, s, cur+1)
        if lh == 1:
            dfs(hh, hl, lh-1, ll, i+1, s, cur)
    else:
        if hl == 1:
            dfs(hh, hl-1, lh, ll, i+1, s, cur)
        if ll == 1:
            dfs(hh, hl, lh, ll-1, i+1, s, cur)


T = int(input())

for it in range(T):
    s = input()
    n = len(s)
    f = [[-1]*16 for _ in range(n)]
    if s[0]=='I':
        f[0][1<<0] = 0
        f[0][1<<1] = 0
    else:
        f[0][1<<2] = 0
        f[0][1<<3] = 0 
    #print(f[0])
    for i in range(1, n):
        for j in range(16):
            if f[i-1][j] != -1:
                if s[i] == "I":
                    if (j & (1<<0)) == 0:
                        f[i][j|(1<<0)] = max(f[i-1][j],f[i][j|(1<<0)])
                    if (j & (1<<1)) == 0:
                        f[i][j|(1<<1)] = max(f[i-1][j],f[i][j|(1<<1)])
                elif s[i] == "i":
                    if (j & (1<<2)) == 0:
                        f[i][j|(1<<2)] = max(f[i-1][j], f[i][j|(1<<2)])
                    if (j & (1<<3)) == 0:
                        f[i][j|(1<<3)] = max(f[i-1][j], f[i][j|(1<<3)])
                elif s[i] == "O":
                    if j & (1<<0): #一开始写成了==1
                        f[i][j - (1<<0)] = max(f[i-1][j] + 1, f[i][j-(1<<0)])
                    if j & (1<<2):
                        f[i][j - (1<<2)] = max(f[i-1][j], f[i][j-(1<<2)])
                else: #s[i] = 'o'
                    if j & (1<<1):
                        f[i][j - (1<<1)] = max(f[i-1][j], f[i][j-(1<<1)])
                    if j & (1<<3):
                        f[i][j - (1<<3)] = max(f[i-1][j], f[i][j-(1<<3)])
        #print(f[i])
    #dfs(0, 0, 0, 0, 0, s, 0)

    ans = max(max(f[-1]),0)
    print("Case #%d: %d"%(it+1, ans))