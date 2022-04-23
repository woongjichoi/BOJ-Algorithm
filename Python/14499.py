import sys
input=sys.stdin.readline

n,m,x,y,k=map(int, input().split())
board=[list(map(int, input().split())) for _ in range(n)]
operations=list(map(int, input().split()))

#dice=[0]*6
temp=[4,2,1,5,6,3]
d={4:0,2:0,1:0,5:0,6:0,3:0}

for operation in operations:
    if operation==1: # 동쪽
        if y+1<0 or y+1>=m:
            continue
        y+=1
        a = temp[0]
        temp[0] = temp[4]
        temp[4] = temp[5]
        temp[5] = temp[2]
        temp[2] = a
    elif operation==2: # 서쪽
        if y-1<0 or y-1>=m:
            continue
        y-=1
        a = temp[4]
        temp[4] = temp[0]
        temp[0] = temp[2]
        temp[2] = temp[5]
        temp[5] = a
    elif operation==3: # 북쪽
        if x-1<0 or x-1>=n:
            continue
        x-=1
        a = temp[1]
        temp[1] = temp[2]
        temp[2] = temp[3]
        temp[3] = temp[4]
        temp[4] = a
    else: # 남쪽
        if x+1<0 or x+1>=n:
            continue
        x+=1
        a=temp[4]
        temp[4]=temp[3]
        temp[3]=temp[2]
        temp[2]=temp[1]
        temp[1]=a
    if board[x][y]==0:
        board[x][y]=d[temp[4]]
    else:
        d[temp[4]]=board[x][y]
        board[x][y]=0
    print(d[temp[2]])
