import sys
input=sys.stdin.readline

n=int(input())
love=[]
for i in range(n*n):
    love.append(list(map(int, input().split())))

seat=[[0]*n for _ in range(n)]

direction=[[0,1],[0,-1],[1,0],[-1,0]]

for i in range(n*n):
    tmp=[]
    for j in range(n):
        for k in range(n):
            if seat[j][k]==0:
                like=0
                empty=0
                for l in range(4):
                    x=j+direction[l][0]
                    y=k+direction[l][1]
                    if x<0 or x>=n or y<0 or y>=n:
                        continue
                    if seat[x][y] in love[i][1:]:
                        like+=1
                    if seat[x][y]==0:
                        empty+=1
                tmp.append([like,empty,j,k])
    tmp.sort(key=lambda x:(-x[0],-x[1],x[2],x[3]))
    seat[tmp[0][2]][tmp[0][3]]=love[i][0]

#print(seat)

love.sort()
#print(love)

answer=0

for i in range(n):
    for j in range(n):
        satisfaction=0
        for k in range(4):
            x=i+direction[k][0]
            y=j+direction[k][1]
            if x<0 or x>=n or y<0 or y>=n:
                continue
            if seat[x][y] in love[seat[i][j]-1][1:]:
                satisfaction+=1
        if satisfaction==0:
            answer+=0
        elif satisfaction==1:
            answer+=1
        elif satisfaction==2:
            answer+=10
        elif satisfaction==3:
            answer+=100
        elif satisfaction==4:
            answer+=1000

print(answer)
