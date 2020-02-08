from bisect import bisect_left, bisect_right, insort_left,  insort_right
from string import ascii_lowercase
from heapq import heappush, heappop, heapify
from collections import Counter, defaultdict
from itertools import product

T = int(input())

for it in range(T):
    n = int(input())
    p = list(map(int, input().split()))
    ans = [] 
    sale_flag = [True] * (n*2)
    for i, num in enumerate(p):
        if sale_flag[i]:
            idx = bisect_left(p, num/3*4, lo=i+1)
            #若已被标记 向后移动
            #while sale_flag[idx] == True:#因为必定有解 不做idx<n 与 前后相等的check
            while idx<2*n and sale_flag[idx]==False:
                idx += 1 
            #print(num, idx)
            sale_flag[idx] = False
            ans.append(num)

    print("Case #%d: %s"%(it+1, ' '.join(map(str,ans))))
    
    #print(ans) Case #2: [9, 9, 12, 15]