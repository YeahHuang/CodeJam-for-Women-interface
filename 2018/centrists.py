from bisect import bisect_left, bisect_right, insort_left,  insort_right
from string import ascii_lowercase
from heapq import heappush, heappop, heapify
from collections import Counter, defaultdict
from itertools import product
"""
名字： 长度L的全大写 均不同

首先把开头相等的substr都去掉
当前位： 若均distinct 则3个YES
若两个相等 则第3个必然NO
而这两个呢 把除了第一个的相同部分删掉 

若剩下的第一位不是 头1 & 头2 两个都YES
否则 是和头2相等的 必须是No
我们就模拟一下前俩的顺序 看看有木有可能在中间即可 
可能有漏考虑的情况 晚点再说
10:52 WA 11:06先看后面的
11:17 卡在了RE 不知所措
"""
T = int(input())

for it in range(T):
    l = int(input())
    s = list(input().split())
    f = ["YES"] * 3 
    i = 0 
    while i<l and s[0][i] == s[1][i] and s[0][i] == s[2][i]:
        i += 1 
    #i: first_distinct_index
    #因为说了名字distinct 所以其实这里不用check i < l 的
    if i==l:
        continue
    if s[0][i]!=s[1][i] and s[0][i]!=s[2][i] and s[1][i]!=s[2][i]: #若均distinct
        f = ["YES"] * 3
    else: #若有2个相等
        if s[0][i]==s[1][i]:
            q, p1, p2 = 2, 0, 1
        elif s[1][i] == s[2][i]:
            q, p1, p2 = 0, 1, 2
        else: #s[0]==s[2]
            #q, p1, p2 = 2, 0, 1   11:07加备注的时候发现的bug 以后注意呀 
            q, p1, p2 = 1, 0, 2
        f[q] = "NO"
        j = i + 1
        while j<l and s[p1][j] == s[p2][j]:  #j: secend_distinct_index
            j += 1
        if j == l:
            continue
        if s[p1][j] == s[q][i] and s[p2][j] == s[p2][i]:
            f[p1] = "YES"
            f[p2] = "NO"        
        elif s[p2][j] == s[q][i] and s[p1][j] == s[p2][i]:
            f[p2] = "YES"
            f[p1] = "NO"
        else:
            f[p1] = "YES"
            f[p2] = "YES"

    print("Case #%d: %s"%(it+1, " ".join(f)))