'''
5 9 AK

'''
# -*- coding:utf-8 -*-
import copy 
import pprint as pp
from functools import reduce
import math


T = int(input())

debug = True

for i in range(T): # 该模版 这里为iter
    k = int(input())

    qpp = input().split(" ")
    d = [int(qpp[j]) for j in range(len(qpp))]
    d.sort()

    ans = 0
    if k%2==0:
        for j in range(k//2):
            ans += pow(j-d[j*2],2) + pow(j-d[j*2+1],2)
    else:
        for j in range((k-1)//2):
            ans += pow(j-d[j*2],2) + pow(j-d[j*2+1],2)
        ans += pow((k-1)//2-d[k-1],2)
    print("Case #%d: %d"%(i+1, ans))
