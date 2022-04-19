import sys
input=sys.stdin.readline

import copy

n,m=map(int, input().split())
board=[list(map(int, input().split())) for _ in range(n)]
moves=[list(map(int, input().split())) for _ in range(m)]
directions=[[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]

def magic(d,s):
    global board, clouds
    # 1.
    x=directions[d-1][0]
    y=directions[d-1][1]
    for cloud in clouds:
        cloud[0]=(n+cloud[0]-x*s)%n
        cloud[1]=(n+cloud[1]-y*s)%n

    # 2. & 3.
    visited=[[False]*n for _ in range(n)]
    for cloud in clouds:
        board[cloud[0]][cloud[1]]+=1
        visited[cloud[0]][cloud[1]]=True
    water_copy=copy.deepcopy(clouds)
    clouds.clear()

    # 4.
    diagonal=[[-1,-1],[-1,1],[1,-1],[1,1]]
    for cloud in water_copy:
        count=0
        for diagon in diagonal:
            x=cloud[0]+diagon[0]
            y=cloud[1]+diagon[1]
            if x<0 or x>=n or y<0 or y>=n:
                continue
            if board[x][y]>0:
                count+=1
        board[cloud[0]][cloud[1]]+=count

    # 5.
    for i in range(n):
        for j in range(n):
            if board[i][j]>=2 and visited[i][j]==False:
                clouds.append([i,j])
                board[i][j]-=2


clouds=[[n-1,0],[n-1,1],[n-2,0],[n-2,1]]
for i in range(m):
    magic(moves[i][0],moves[i][1])

answer=0
for i in range(n):
    answer+=sum(board[i])

print(answer)