from bisect import bisect_left, bisect_right, insort_left,  insort_right
from string import ascii_lowercase
from heapq import heappush, heappop, heapify
from collections import Counter, defaultdict
from itertools import product

"""
desirable parcel: 存在 不用连续的 3个marks s.t. 峰状

小数据集 枚举 2^n  + n*n预处理
    
    大数据集 模拟dp 后面的显然和前面的都是独立的 
    可以贪心 因为一旦存在 肯定先放个卡？ 验证成功

    但需要check一下 最后的那个放了之后 后面的能否成行 
    最终复杂度O（n*n）

"""

T = int(input())

for it in range(T):
    k = int(input()) + 1
    m = list(map(int, input().split()))

    #left_small, left_big, right_small, right_large
    f = [[-1, -1, k, k] for i in range(k)]
    for i in range(k):
        for j in range(i-1, -1, -1):
            if m[j] < m[i]:
                f[i][0] = j
                break
        for j in range(i-1, -1, -1):
            if m[j] > m[i]:
                f[i][1] = j
                break
        for j in range(i+1, k):
            if m[j] < m[i]:
                f[i][2] = j
                break
        for j in range(i+1, k):
            if m[j] > m[i]:
                f[i][3] = j
                break 
    #print(k,f)
    cur_left, cur_right = 0, k-1

    #尝试贪心先 不可以 因为必须两边都符合
    ans = 0
    for i in range(1, k-1):
        if cur_right == i:
            ans += 1
            cur_left, cur_right = cur_right, k-1
            continue
        if (f[i][0]>=cur_left and f[i][2]<cur_right):
            cur_right = f[i][2]
        if (f[i][1]>=cur_left and f[i][3]<cur_right):
            cur_right = f[i][3]

    flag = False
    for i in range(cur_left+1, k-1):
        if (f[i][0]>=cur_left and f[i][2]<=cur_right) or (f[i][1]>=cur_left and f[i][3]<=cur_right):
            flag = True
            break
    if flag == False:
        ans -= 1 
    print("Case #%d: %d"%(it+1, ans))