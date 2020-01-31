#-*- coding:utf-8 -*-
'''
平均分布 
两种 Cn k1 * C(n-k1) k1 ...


内部排列  
'''

def C(n, k):
    Cnk = 1
    if (n-k)<k :
        k = n-k
    for i in range(1,k+1):
        Cnk = Cnk * (n-i+1) / i 
    return Cnk

def GetAns(n, k):
    ans = 1
    nk = int(n/k)
    num1 = n-int(nk)*k
    num0 = k-num1
    res = n
    for j in range(num1):
        ans *= C(res,nk+1)
        res -= nk + 1
    ans = ans / jie[num1]
    for j in range(num0):
        ans *= C(res, nk)
        res -= nk
    ans = ans / jie[num0]
    if debug:
        print("res=%d num0=%d num1=%d ans0=%d"%(res, num0, num1, ans))
    ans *= (ansIn[nk]**num0) * (ansIn[nk+1]**num1)
    return ans
    

debug = False
T = int(input())
jie = [1 for i in range(21)]
ansIn = [1 for i in range(22)] # 一开始写的是range(21) 这样 ansIn[nk+1] 在n=20 k=1 时就会RE 

for i in range(2,21):
    jie[i] = jie[i-1] * i
for i in range(3, 21):
    ansIn[i] = jie[i] / i / 2
if debug:
    print(jie)
    print(ansIn) # 依然经常情不自禁的把print写成c++里的print
    print(GetAns(1,1))

for i in range(T):
    string = input()
    if debug:
        print("string=%s"%string)
    qpp = string.split(" ")
    n = int(qpp[0])
    k = int(qpp[1])
    print("Case #%d: %d"%(i+1, GetAns(n, k)))

