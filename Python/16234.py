import sys
input=sys.stdin.readline

n,l,r=map(int,input().split())
population=[list(map(int,input().split())) for _ in range(n)]

from collections import deque

directions=[[0,-1],[0,1],[1,0],[-1,0]]
answer=0

# 같은 연합 구하기 
def bfs(i,j):
    temp=[]
    temp.append([i,j])
    queue=deque(temp)
    queue.append([i,j])
    while queue:
        a,b=queue.popleft()
        for direction in directions:
            x=a+direction[0]
            y=b+direction[1]
            if x<0 or x>=n or y<0 or y>=n:
                continue
            if abs(population[a][b]-population[x][y])>=l and abs(population[a][b]-population[x][y])<=r and visited[x][y]==False:
                visited[x][y]=True
                queue.append([x,y])
                temp.append([x,y])

    return temp


while True:
    visited=[[False]*n for _ in range(n)]

    flag=0
    
    for i in range(n):
        for j in range(n):
            if visited[i][j]==False:
                visited[i][j]=True

                unions=bfs(i,j)

                if unions==[[i, j]]:
                    continue

                flag=1

                part_sum=0
                for union in unions:
                    part_sum+=population[union[0]][union[1]]

                for union in unions:
                    population[union[0]][union[1]]=part_sum//len(unions)

    if flag==0:
        break

    answer+=1

print(answer)
