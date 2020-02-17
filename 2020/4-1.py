from bisect import bisect_left, bisect_right, insort_left,  insort_right
from string import ascii_lowercase
from heapq import heappush, heappop, heapify
from collections import Counter, defaultdict
from itertools import product
from random import randint
from operator import add
from re import split, sub
import numpy as np
def coss_multi(v1, v2):
    """
    计算两个向量的叉乘
    :param v1:
    :param v2:
    :return:
    """
    return v1[0]*v2[1] - v1[1]*v2[0]
 
 
def polygon_area(polygon):
    """
    计算多边形的面积，支持非凸情况
    :param polygon: 多边形顶点，已经进行顺次逆时针排序
    :return: 该多边形的面积
    """
    n = len(polygon)
 
    if n < 3:
        return 0
 
    vectors = np.zeros((n, 2))
    for i in range(4):
        vectors[i, :] = polygon[i, :] - polygon[0, :]
 
    area = 0
    for i in range(1, n):
        tmp = coss_multi(vectors[i-1, :], vectors[i, :]) 
        if tmp >=1 or tmp<=-1:
            area += tmp
        else:
            print(tmp)
            return 0

    return area

def PolygonArea(corners):
    x1, x2, x0 = corners[0][0], corners[2][0], corners[1][0]
    y1, y2, y0 = corners[0][1], corners[2][1], corners[1][1]
    p1 = (x2-x1)*(y0-y1)-(y2-y1)*(x0-x1)
    x0, y0 = corners[3][0], corners[3][1]
    p2 = (x2-x1)*(y0-y1)-(y2-y1)*(x0-x1)
    if p1*p2 >= 0:
        return 0
    last = (corners[3][0] - corners[0][0], corners[3][1] - corners[0][1])
    for i in range(3):
        a = (corners[i+1][0] - corners[i][0], corners[i+1][1] - corners[i][1])
        if a[0] * last[1] == a[1] * last[0]:
            return 0
        last = a
    n = len(corners) # of corners
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]

    area = abs(area) 
    return area





T = int(input())

for it in range(T):
    n = int(input())
    f = []
    for i in range(n):
        x, y = map(int, input().split())
        f.append([x,y])
    ans = 1e9 * 1e9 * 10
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1, n):
                for l in range(k+1,n):
                    polygon = [f[i], f[j], f[k], f[l]]
                    qpp = abs(PolygonArea(polygon))
                    if qpp >= 1:
                        ans = min(ans, qpp)
                        #continue
                    
                    polygon[2],polygon[1] = polygon[1], polygon[2]
                    qpp = abs(PolygonArea(polygon))
                    if qpp >= 1:
                        ans = min(ans, qpp)
                        #continue
                    polygon[2], polygon[3] = polygon[2], polygon[3]
                    qpp = abs(PolygonArea(polygon))
                    if qpp >= 1:
                        ans = min(ans, qpp)

                    
    print("Case #%d: %d"%(it+1, ans))