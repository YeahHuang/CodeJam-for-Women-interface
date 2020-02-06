import collections

"""
思路总结：
纯暴力 - 过small数据集
把2*v<k 的情况中的中间一坨公式算一下 - 过medium数据集
把2*v<k 的两头公式算一下 - 过全部数据集


关键就是要耐心的算公式 细心 细心 再细心 
debug花时间比较久的是公式+-的符号问题  以后注意

2*v<k 

0..v  0..r+v  max(0, r-v, g-v)    min(r+v, g+v, k)
                max(0, g-v)     min(r+v, g+v) = min(g,r) + v
      0..v          0           min(g,r) + v        
      v+1..v+r      g-v         min(g,r) + v


v+1..k-v-1 r-v..r+v  max(r-v, g-v) min(r+v, g+v)
    
     g:   r-v..r      r - g + 2*v + 1
     g:   r+1..r+v    g - r + 2*v + 1 

        (2*v+1) * (2*v+1) +   v + (v-1)... + 0 + 1 + 2 +...v
        = (2v+1) * (2v+1) + (1+v)*v/2*2
        = (2v+1) * (2v+1) + (1+v)*v

k-v..k    r-v..k  max

k-v-1 - v-1+1
k-2v-1

2*v>k:
        max(0, r-v)   min(r+v, k)            max(0, r-v,g-v)  min(r+v, g+v, k)
"""

T = int(input())

for it in range(T):
    k, v = map(int,input().split())
    ans = 0 
    if 2*v < k:
        
        """
        #version1: slowest
        for r in range(v+1): #0..v
            for g in range(0, r+v+1): #0..r+v
                ans += min(r,g) + v - max(0, g-v) + 1

        #version2: 去掉min() max()
        for r in range(v+1): #0..v
            for g in range(0, r+1): #0..r
                ans += g + v + 1  #g < r r <=v g<v g - v < 0 
            for g in range(r+1, v+1): #r+1..v
                ans += r + v + 1
            for g in range(v+1, r+v+1): #v+1..r+v
                ans += r + 2*v - g + 1
        
        #version3 用sum去解决中间的f(r)
        for r in range(v+1): #0..v
            for g in range(0, r+1): #0..r.   0+1+2+..r
                ans += g 
            for g in range(r+1, v+1): #r+1..v  r*(v-r)
                ans += r
            for g in range(v+1, v+r+1): #v+1..r+v    
                ans += r + v - g 
                #(v+r)*r - sum(v+1..v+r) = (v+r)*r - v*r - (1+2+3..+r) = r*r - (1..r)
            #一共 = (1+2..+r) + r*v - r*r + r*r - (1...r) = r*v
            #所以f(r) = r*v   （1+2+3..v) * v
            #f(r) = (v+1)*(r+v+1) + r*v
             = (v+1)*(v+1) + (2*v+1)*r 
        """
        ans += (v+1) * (v+1)*(v+1) + (v+1)*v/2*(2*v+1) #得到最终公式
        ans *= 2
        ans += ((2*v+1) * (2*v+1) - v * (v+1)) * (k-2*v-2+1)
        """
        一开始 + -  弄反了 debug了很久 后来拆分着debug公式 才OK 
        ans += (2*v+1) * (2*v+1) + v * (v+1)
        #ans += (2*v+1)*(2*v+1)*(k-2*v-1)
        #ans += ((2*v+1) * (2*v+1) + v * (v+1)) * (k-2*v-2+1)
        
        (2v +1) * （k-2v-1) 
        r>g  g-r     1+2+3...v
        r<g  r-g     1+2+3...v 
        (1+v)*v
        
        for r in range(v+1, k-v): #v+1.. k-v-1
            for g in range(r-v, r):
                ans += g - r
            for g in range(r, r+v+1): #r-v .. r+v
                ans += r - g 
        """
    else:
        for r in range(k+1):
            for g in range(max(0, r-v), min(r+v, k)+1):
                ans += min(r+v, g+v, k) - max(0, r-v, g-v) + 1
    print("Case #%d: %d"%(it+1, ans))


  