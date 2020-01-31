"""
1. 无序 -> 排序sort
2. 一个是当前取的问题 一个是剩下的问题
    2.1 当前取 m个的话 就是 1 * C(n-1)(m-1) 当前的排序可能是个问题
    2.2 剩下的话 就直接dp  （n-m) (k-1) 即可 其中 m = n//k 
3. 关于当前排序 
    m = 1   1
    m = 2   1
    m = 3   1   2 * 1 / 2 
    m = 4   3   3*2*1/2 = 3
    m = 5       4*3*2*1/2=12
                （m-1) ! / 2 
"""
import collections

T = int(input())

f = [[1 for k in range(21)] for n in range(21)]

jie = [1]
for i in range(1, 21):
    jie.append(jie[i-1]*i)

#print(jie)

for n in range(2,21):
    for k in range(1, n+1):
        m = n // k
        f[n][k] = f[n-m][k-1] * jie[n-1] / jie[n-m]
        if m >= 3:
            f[n][k] /= 2
        if n % k > 0:
            m += 1
            if m >= 3:
                f[n][k] += f[n-m][k-1] * jie[n-1] / jie[n-m] / 2
            else:
                f[n][k] += f[n-m][k-1] * jie[n-1] / jie[n-m] 

for it in range(T):
    n, k = map(int,input().split())
    print("Case #%d: %d"%(it+1, f[n][k]))