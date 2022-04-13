# 반례: https://www.acmicpc.net/board/view/72795

import sys
input=sys.stdin.readline

from collections import deque

n,m=map(int, input().split())
r,c,d=map(int, input().split())
robots=[list(map(int, input().split())) for _ in range(n)]
visited=[[0]*m for _ in range(n)]
#directions=[[-1,0],[0,-1],[1,0],[0,1]]
directions=[[-1,0],[0,1],[1,0],[0,-1]]

answer=0

def bfs(p,q,z):
    queue=deque([[p,q,z]])
    count=0

    while queue:
        i,j,k=queue.popleft()
        
        visited[i][j]=1 
    
        if count==4: 
            if robots[i-directions[k][0]][j-directions[k][1]]==1:
                return
            else:
                queue.append([i-directions[k][0],j-directions[k][1],k])
                count=0
                continue
            
        next_d=directions[(k-1)%4] 
        x=i+next_d[0]
        y=j+next_d[1]
        if 0<=x<n and 0<=y<m and robots[x][y]==0 and visited[x][y]==0:
            k=directions.index(next_d)
            queue.append([x,y,k])
            count=0
        else:
            k=directions.index(next_d)
            queue.append([i,j,k])
            count+=1
        #print(queue)
        #print(count)
        #print(visited)

bfs(r,c,d)

for i in range(n):
    for j in range(m):
        if visited[i][j]==1:
            answer+=1

print(answer)
