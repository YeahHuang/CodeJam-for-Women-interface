T = int(input())
for i in range(T):
    b = int(input())
    string = input() # 一开始不小心打错成了intput
    ans = ""
    if len(string)!=8*b:
        print("ERROR! len(string)=%d , 8*b=%d"%(len(string),8*b))
        continue
    for j in range(1,b+1):
        qpp = 0
        for k in range(8):
            if string[8*j-k-1]=='I':
                qpp += 1<<k
        ans+=chr(qpp)
    print("Case #%d: %s"%(i+1, ans))

#一次KO 棒！