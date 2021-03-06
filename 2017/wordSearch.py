from bisect import bisect_left, bisect_right, insort_left,  insort_right
from string import ascii_lowercase
from heapq import heappush, heappop, heapify
from collections import Counter, defaultdict
from itertools import product
"""
找到各个方向的I/O
需要刚好N个I/O 不能多于D rows or columns


小数据集： 构造

2‘06开始
1'49读题结束 似乎算出来了
1'34 开始写小的

3m - 4(3<=m<=15) -> 41 (1, 2, 5, 8, ...41)
后面的 3m-3 (1<m<15) (1,3,6,9,...39, 41)

/ 的 j:  1, 3, 5, 7 ...
O 的 j:  0, 4, 8, 12 ..
I 的 j： 2, 6, 10, 14..
16min AC


"""


def judge(c1, c2):
    return (c1=="I" and c2=="O") or (c1=="O" and c2=="I")

def check(f):
    cnt = 0 
    for i in range(15):
        for j in range(20):
            if f[i][j] == "/":
                #print(i, j)
                if 0<i<14:
                    cnt += judge(f[i-1][j], f[i+1][j])
                    if 0<j<19:
                        cnt += judge(f[i-1][j-1], f[i+1][j+1])
                        cnt += judge(f[i-1][j+1], f[i+1][j-1])
                if 0<j<19:
                    cnt += judge(f[i][j-1], f[i][j+1])
    return cnt




T = int(input())

for it in range(T):
    d, n = map(int, input().split())
    ans = 0
    f = [["I" for _ in range(20)] for _ in range(15)]
    m, extra = 0,0 
    #general part
    if n<=41:
        if n < 5:
            extra = n
        else:
            m = (n + 4) // 3
            for i in range(m):
                f[i][0] = "O"
                f[i][1] = "/"
            if m<15:
                f[m][2] = "O"
            extra = n - (3 * m - 4)
    else:
        col, n = n // 41, n % 41
        #former col 
        for j in range(1, 2*col, 2):
            for i in range(15):
                f[i][j] = "/"        
        for j in range(0, 2*col+2, 4): #0..2*col+1
            for i in range(15):
                f[i][j] = "O"
        #calculate extra
        if n < 6:
            extra = n
        else:
            m = (n+3)//3
            extra = n - (3*m - 3)
        #print(m, n, extra)
        #last col
        if col & 1:
            j = 2*col+2
            for i in range(m):
                f[i][j] = "O"
        else:
            f[m][2*col+2] = "O"
        j = 2*col + 1
        for i in range(m):
            f[i][j] = "/"

    #extra part
    for i in range(0, extra*2, 2): 
        f[i][-2] = "/"
        f[i][-3] = "O"

    print("Case #%d:"%(it+1))
    for i in range(15):
        print("".join(f[i]))
    #print(check(f))