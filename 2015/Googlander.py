"""
1.  直接dfs 每一个宫格*2 也就是2*20  估计也不会超时
2. dp 转过去之后就是一个小的了

Never Never Give Up

dp公式：
f[r][c] = sum([f[c-1][i] for i in range(1, r+1)])
ps 因为可证明/猜测的对称性 在coding时可以写为f[i][c-1]

"""

import collections

T = int(input())
f = [[0]*26 for _ in range(26)]
for i in range(26):
    f[i][1] = f[1][i] = 1

for r in range(2,26):
    for c in range(2, 26):
        for i in range(1,r+1):
            f[r][c] += f[i][c-1]

for it in range(T):
    r, c = map(int, input().split())
    print("Case #%d: %d"%(it+1, f[r][c]))
