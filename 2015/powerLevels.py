"""
10:33 完成读题
虽然看起来大 但是实际小数据集可以找规律的
11:25 KO小数据集 注意要去写代码 不要自己手动算去找规律

11:48 KO
"""

def cnt(num):
    tmp = 9000
    mul = 1
    while tmp > 0:
        mul *= tmp
        tmp -= num
    return len(str(mul))

pre = 19
f = [0] * 31684
for num in range(1990, 9000):
    if cnt(num) != pre:
        #print(cnt(num), num)
        f[cnt(num) + 1] = num
        pre = cnt(num)
pre = 0 
for num in range(1,1990): #一开始num从0开始 直接死循环了 
    qpp = cnt(num)
    #print(qpp, num)
    if qpp != pre:
        f[qpp + 1] = num
        pre = qpp


i = 20
while i<31683:
    while f[i+1] == 0:
        f[i+1] = f[i]
        i += 1
    i += 1
#print(f)



"""
num = 9000 - 1      4
num = 9000 - 2      5
num = 9000 - 11     5
num = 9000 - 12     6



9000 - 1
num = 1989  19
num = 1990  18
num = 1991  18
"""



T = int(input())

for it in range(T):
    n = int(input())
    if n>31683:
        n = 31683
    if n<=4:
        ans = "..."
    else:
        ans = "IT'S OVER 9000"+'!'*f[n]
    print("Case #%d: %s"%(it+1, ans))
