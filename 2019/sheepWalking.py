from bisect import bisect_left, bisect_right, insort_left,  insort_right
from string import ascii_lowercase
from heapq import heappush, heappop, heapify
from collections import Counter, defaultdict
from itertools import product

"""
初步探索： 
f(1,0) = (f(0,0)+f(1,1))/2  + 1
f(1,1) = (f(1,0)+f(0,1))/2  + 1
f(1,0) = f(0,1)
>> 得到 f(1,0) = 3.0   f(1,1) = 4.0

进一步归一化：
f(i,0) = (f(i-1,0)+f(i,1))/2 + 1
f(i,1) = (f(i-1,1)+f(i,0))/2 + 1
>> 得到f(i,0) = (f[i-1][0]/2 + f[i-1][1]/4 + 1.5) * 4 / 3 

对于剩下的(i>=2, j>=2)：
f(i,j) = (f(i-1,j)+f(i,j-1))/2 + 1

需要注意的tips：
1. 我一开始只算了f[0][i] f[i][1] 忘记更新f[i][0] f[1][i] 了 以后注意
2. 我一开始公式推导错误 而且因为一开始算错 还一直看test case也找不出来 卡了30min+ 还好最后重新核算 发现了 以后一定谨慎
"""
def func(s):
    return abs(int(s))

T = int(input())

for it in range(T):
    x, y = map(func, input().split())
    x, y = max(x,y), min(x,y)
    #ans = 0.0
    f = [[0.0]*(600) for _ in range(600)]
    f[1][0] = f[0][1]= 3.0
    f[1][1] = 4.0
    for i in range(2, x+1):
        f[i][0] = f[0][i] = f[i][0] = (f[i-1][0]/2 + f[i-1][1]/4 + 1.5) * 4 / 3  #一开始+0.5 调了很久没弄出来
        f[1][i] = f[i][1] = (f[i-1][1] + f[i][0]) / 2 + 1

    for i in range(2, x+1):
        for j in range(2, y+1):
            f[i][j] = (f[i-1][j]+f[i][j-1])/2 + 1
    #print(f)
    print("Case #%d: %.6f"%(it+1, f[x][y]))