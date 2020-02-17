from bisect import bisect_left, bisect_right, insort_left,  insort_right
from string import ascii_lowercase
from heapq import heappush, heappop, heapify
from collections import Counter, defaultdict
from itertools import product
from random import randint, shuffle
from operator import add
from re import split, sub
from copy import deepcopy
"""
10:58开始
5min读题
11:20 WA
最小的 包括hidden 直接枚举？
11:44 第二次提交 过了

"""

def pre(s):
    return int(s)-1

def opp(c):
    return ["L","R"][c=="L"]

global f, ans, x,flag

def dfs(step):
    global f,x, n, flag,ans
    if step == n:
        flag = True
        ans = deepcopy(f)
        return
    #print(step, f, flag)
    if flag == False:
        if x[step]!=-1 and -1<x[step+1]<step:
            if (f[x[step]] != f[x[step+1]]):
                f[step] = opp(f[x[step]])
                f[step+1] = opp(f[step])
                #print("both",step, x[step], x[step+1], f)
                dfs(step+2)
            else:
                return
        elif x[step]!=-1:
            f[step] = opp(f[x[step]])
            f[step+1] = opp(f[step])
            #print("step",step, x[step], x[step+1], f)
            dfs(step+2)
        elif -1<x[step+1]<step:
            f[step+1] = opp(f[x[step+1]])
            f[step] = opp(f[step+1])
            #print("step+1",step, x[step], x[step+1], f)
            dfs(step+2)
        else:
            f[step], f[step+1] = "L", "R"
            dfs(step+2)
            f[step], f[step+1] = "R", "L"
            dfs(step+2)

def check(a, n, f):
    for i in range(0, n, 2):
        if (f[i] == "L" and f[i+1]=="L") or (f[i] == "R" and f[i+1]=="R"):
            return False
        if (f[a[i]] == "L" and f[a[i+1]]=="L") or (f[a[i]] == "R" and f[a[i+1]]=="R"):
            return False
    return True

test_mode = True

if test_mode == False:
    T = int(input())
else:
    T = 100
    n = 1000
    a = [i for i in range(1000)]

for it in range(T):
    if test_mode:
        #a = [2, 4, 0, 1, 5, 3]
        shuffle(a)
        #print(a)
    else:
        n = int(input())
        a = list(map(pre, input().split()))
    x = [-1]*n #限制
    for i in range(0,n,2):
        #print(max(a[i],a[i+1]), min(a[i],a[i+1]))
        x[max(a[i],a[i+1])] = min(a[i],a[i+1])
    f = ["L"]*n
    f[1] = "R"
    flag = False
    if n > 2:
        dfs(2)
    else:
        ans = ["L","R"]
    if test_mode:
        if check(a, n, ans) == False:
            print("Case #%d: %s"%(it+1, "".join(ans)))
            print(a,x)
    else:
        print("Case #%d: %s"%(it+1, "".join(ans)))