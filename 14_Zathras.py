'''
A个a。B个b   alpha  beta不变
K = min(A, B)
2%(round down) of K couples.-> 1 baby
alpha%(round down) 的孩子是A  beta%(round down)的孩子是B
剩下的是A B 平分， 如果剩下的是奇数， 则为B

Decommissioning:
在新的Z出生之前， 1%的a 1%的b 会decommissioning 两天后就会解体。

所以d1 做决定 d2 生 d3 挂。  1234
'''

T = int(input()) # yeah! 自己AK了大数据集！ 关键是要能够发现是有上线的 不用推公式 它是会收敛的！
debug = False
for  i in range(T):
    qpp = input().split(" ") # 一开始直接 A, B, a, b, Y = input().split(" ") 忘记type问题了
    A = int(qpp[0])   
    B = int(qpp[1])
    a = int(qpp[2])# 一开始 a = float(qpp[2])*0.01 要注意float的精准性要远远比int低 改为int后计算就对了
    b = int(qpp[3])
    Y = int(qpp[4])
    for j in range(Y):
        K = min(A, B) #K = 12345 
        babies = int(K*0.02)
        babyA = int(babies * a / 100)   #一开始这里写成了alpha 注意注解和真实变量名的对应 
        babyB = int(babies * b / 100 ) 
        if debug:
            print("babyA1 = %d, babyB1 = %d"%(babyA, babyB))
        remain = int(babies - babyA - babyB)
        babyA += int(remain/2)
        babyB += remain - int(remain/2)
        decA = int(A*0.01) # 一开始没有int() 直接 decA = A/100。你会发现float 和 int的墙纸转化中就会出错哦
        decB = int(B*0.01) 
        if debug:
            print("babyA2 = %d, babyB2 = %d.  decA = %d, decB=%d"%(babyA, babyB, decA, decB))
        A = A + babyA - decA
        B = B + babyB - decB 
        if (babyA==decA and babyB==decB):
            #print("iteration=%d"%(j+1))
            break
    # 一开始语法错误 写成了  print("Case #%d: %d %d", i+1, A, B) 和C++语法搞混了
    print("Case #%d: %d %d"%(i+1, A, B))
