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
        if len(x[step]):
            biao = list(x[step])[0]
            for c in x[step]:
                if f[c] != f[biao]:
                    return
        if len(x[step+1]):
            biao1 = list(x[step+1])[0]
            for c in x[step+1]:
                if f[c] != f[biao1]:
                    return

        if len(x[step]) and len(x[step+1]):
            if (f[biao]!=f[biao1]):
                f[step] = opp(f[biao])
                f[step+1] = opp(f[step])
                #print("both",step, x[step], x[step+1], f)
                dfs(step+2)
            else:
                return
        elif len(x[step]):
            f[step] = opp(f[biao])
            f[step+1] = opp(f[step])
            #print("step",step, x[step], x[step+1], f)
            dfs(step+2)
        elif len(x[step+1]):
            f[step+1] = opp(f[biao1])
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

test_mode = False

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
    x = [set() for _ in range(n)] #限制
    for i in range(0,n,2):
        #print(max(a[i],a[i+1]), min(a[i],a[i+1]))
        if a[i]//2!=a[i+1]//2:
            x[max(a[i],a[i+1])].add(min(a[i],a[i+1]))

    for i in range(n-2, -1, -2):
        for p1 in x[i]:
            for p2 in x[i+1]:
                if p1//2 !=p2//2:
                    x[max(p1,p2)].add(min(p1,p2))
        #print(x)

    f = ["L"]*n
    #print(x)
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