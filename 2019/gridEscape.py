from bisect import bisect_left, bisect_right, insort_left,  insort_right
from string import ascii_lowercase
from heapq import heappush, heappop, heapify
from collections import Counter, defaultdict
from itertools import product

"""
1. 纯暴力枚举 4^(R*C) * (R*C) * (R*C) = 2^16 * 64 = 2^64
2, 观察构造 or 暴力的剪枝

最后sol： 观察构造
如果只有1人无法逃出 不可能
剩下的均可构造 具体解释见⬇️
"""

T = int(input())

for it in range(T):
    r, c, k = map(int, input().split())
    no = r*c-k #no表示 无法逃出的数量
    if no==1:  #如果只有1人无法逃出 不可能
        print("Case #%d: IMPOSSIBLE"%(it+1))
        continue

    #剩下的均可构造 先假定所有的都从右下角的S出口逃出 
    print("Case #%d: POSSIBLE"%(it+1))
    f = [["E"]*c for _ in range(r)]
    for i in range(r):
        f[i][-1] = "S"

    if no <= c: #如果要被困住的数量<c 则使用EW死锁
    """
    如 r = 3 c = 5 k = 3 则
     EWWES
     EEEES
     EEEES
    """
        for j in range(1,no):
            f[0][j] = "W"
        f[0][0] = "E"
    else: #否则 使用NS死锁
    """
    如 r = 3 c = 5 k = 9 则
     NWWWWW
     SWWWWS
     EEEEES
    """
        x, y = 0, 0
        for i in range(no):
            #print(x,y)
            if y == 0:
                f[x][y] = "N"
            else:
                f[x][y] = "W"
            if y == c-1:
                x += 1
                y = 0 
            else:
                y += 1
        f[0][0] = "S"
    for i in range(r):
        print("".join(f[i]))
    