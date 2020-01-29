import sys

n = int(input())
for i in range(n):
    s = input()
    print("Case #%d:"%(i+1))
    s1 = '+-'
    for j in range(len(s)):
        s1 += '-'
    s1 += '-+'
    print(s1)
    print('| %s |'%s)
    print(s1)
