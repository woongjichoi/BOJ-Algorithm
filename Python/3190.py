import sys
input=sys.stdin.readline

from collections import deque
visited=deque([]) # visited 이용해서 꼬리 위치도 알 수 있고 직전 위치도 알 수 있음

n=int(input())
board=[['x']*n for _ in range(n)]

apple=int(input())
for i in range(apple):
    a=list(map(int,input().split()))
    board[a[0]-1][a[1]-1]='o'

board[0][0]='s'
visited.append([0,0])

change=int(input())
changes={}
for i in range(change):
    X, C=input().split()
    changes[int(X)]=C
    
count=0

directions=[[0,1],[1,0],[0,-1],[-1,0]]
d=0

while True: 
    if count in changes.keys():
        if changes[count]=='D': # 오른쪽
            d=(d+1)%4 
        else: # 왼쪽
            d=(d-1)%4 
        
    x=visited[-1][0]+directions[d][0]
    y=visited[-1][1]+directions[d][1]

    # 벽에 부딪히거나 자기 몸에 부딪히면 종료 
    if (x<0 or x>=n or y<0 or y>=n) or board[x][y]=='s':
        count+=1
        break
    
    if board[x][y]=='o':
        board[x][y]='s'
        visited.append([x,y])
    else:
        board[x][y]='s'
        visited.append([x,y])
        tail_i,tail_j=visited.popleft()
        board[tail_i][tail_j]='x'
        
    count+=1
    #print(board)
    #print("count", count)
    #print("x", x)
    #print("y", y)
    #print("*****")

print(count)
