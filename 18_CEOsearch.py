''' 8 13 
experience level >=0 

single direct manager > employee

E direct manager for 个 [0,E] 没有传递性 


直接暴力贪心？

'''

import copy 
import pprint as pp
from functools import reduce
import math


T = int(input())

debug = True

for i in range(T):
    L = int(input())
    n = []
    e = []
    cur_left = 0 
    for j in range(L):
        qpp = input().split(" ")
        n.append(int(qpp[0])) 
        e.append(int(qpp[1]))
        leader_num = n[j]*e[j] #改动多次 1:07  AK
        if leader_num>=cur_left:
            cur_left = 0
        else:
            cur_left -= leader_num
        cur_left += n[j]

    ans = max(cur_left, e[L-1]+1)
    
    print("Case #%d: %d"%(i+1, ans))
