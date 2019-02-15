'''
直走 / 右转+前进

'''

import copy #一次KO dp的思想很重要！
import pprint as pp
def isValid(x,y,state0):
    return (0<=x<m and 0<=y<n and state0[x][y])

def getStep(m,n):
    pos = [[m-1, 0]]
    direction = [0]
    state = [[[True for k in range(n) ] for j in range(m)]]
    state[0][m-1][0] = False
    ans = 0
    l = 0
    r = 0
    while (l<=r):
        x = pos[l][0]
        y = pos[l][1]
        dir0 = direction[l]
        dir1 = turnRight[dir0]
        x0 = x+dx[dir0]
        y0 = y+dy[dir0]
        x1 = x+dx[dir1]
        y1 = y+dy[dir1]
        state0 = copy.deepcopy(state[l])
        state1 = copy.deepcopy(state[l])
        if isValid(x0, y0, state0)==False and isValid(x1, y1, state1)==False:
            ans+=1
            if debug:
                pp.pprint(state0)
        elif isValid(x1, y1, state1)==False:
            while isValid(x0,y0, state0):
                state0[x0][y0]=False
                x0 += dx[dir0]
                y0 += dy[dir0]
            x0-=dx[dir0]
            y0-=dy[dir0]
            if isValid(x0+dx[dir0], y0+dy[dir0], state0) or isValid(x0+dx[dir1], y0+dy[dir1],state1):
                print("ERROR! x0=%d y0=%d dir0=%d dir1=%d state0 as belows:"%(x0,y0,dir0,dir1))
                pp.pprint(state0)
            else:
                ans+=1
                if debug:
                    pp.pprint(state0)
        else:

            state1[x1][y1]=False
            pos.append([x1,y1])
            direction.append(dir1)
            state.append(state1)
            r+=1

            if isValid(x0,y0,state0):
                state0[x0][y0]=False
                pos.append([x0,y0])
                direction.append(dir0)
                state.append(state0)
                r+=1

        l+=1
    return ans

dx = [-1, 0, 1,  0]
dy = [0,  1, 0, -1]

turnRight = [1, 2, 3, 0]
debug = False


ans = [[-1 for i in range(26)] for j in range(26)]

for i in range(1,26):
    ans[i][1]=1
    ans[1][i]=1

for m in range(2, 26):
    for n in range(m, 26):
        ans[m][n] = ans[m][n-1]+ans[m-1][n]
        ans[n][m] = ans[m][n]

#print(ans[10][10], ans[9][10], ans[4][9])


T = int(input())
for i in range(T):
    qpp = input().split(" ")
    m = int(qpp[0]) # use m, n to replace r, c  so that we can use l,r to represent bfs()
    n = int(qpp[1])
    print("Case #%d: %d"%(i+1, ans[m][n]))

