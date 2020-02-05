import collections

"""
2*v<k 

0..v  0..r+v  max(0, r-v, g-v)    min(r+v, g+v, k)
                max(0, g-v)     min(r+v, g+v) = min(g,r) + v
      0..v          0           min(g,r) + v        
      v+1..v+r      g-v         min(g,r) + v


v+1..k-v-1 r-v..r+v  max(r-v, g-v) min(r+v, g+v)
    
        r-v..r      r - g + 2*v + 1
        r+1..r+v    g - r + 2*v + 1 

        (2*v+1) * (2*v+1) +   v + (v-1)... + 0 + 1 + 2 +...v
        = (2v+1) * (2v+1) + (1+v)*v/2*2
        = (2v+1) * (2v+1) + (1+v)*v

k-v..k    r-v..k  max


2*v>k:
        max(0, r-v)   min(r+v, k)            max(0, r-v,g-v)  min(r+v, g+v, k)
"""

T = int(input())

for it in range(T):
    k, v = map(int,input().split())
    ans = 0 
    if 2*v < k:
        for r in range(v+1): #0..v
            for g in range(0, r+v+1): #0..r+v
                ans += min(r,g) + v - max(0, g-v) + 1
        ans *= 2
        #ans += (2*v+1) * (2*v+1) + v * (v+1)
        ans += ((2*v+1) * (2*v+1) + v * (v+1)) * (k-2*v-2+1)
        """
        for r in range(v+1, k-v): #v+1.. k-1-1
            for g in range(r-v, r+v+1): #r-v .. r+v
                ans += min(r,g) + 2*v - max(r,g) + 1
        """
    else:
        for r in range(k+1):
            for g in range(max(0, r-v), min(r+v, k)+1):
                ans += min(r+v, g+v, k) - max(0, r-v, g-v) + 1
    print("Case #%d: %d"%(it+1, ans))


  