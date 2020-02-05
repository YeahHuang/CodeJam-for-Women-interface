import collections

T = int(input())

for it in range(T):
    n = int(input())
    s = input()
    ans = ""
    for i in range(n):
        tmp = 0
        for j in range(8):
            tmp += (s[i*8 + j]=='I') * (1<<(7-j))
        #print(tmp)
        ans += chr(tmp)
    print("Case #%d: %s"%(it+1, ans))