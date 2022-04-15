import sys
input=sys.stdin.readline

from collections import deque
import copy

a=deque(list(input().rstrip()))
b=deque(list(input().rstrip()))
c=deque(list(input().rstrip()))
d=deque(list(input().rstrip()))
queue=[a,b,c,d]

n=int(input())
changes=[list(map(int, input().split())) for _ in range(n)]

# 왼쪽 함수랑 오른쪽 함수 분리해야 함 

# 자기도 돌면 a->b->c 이럴 때 a 돌고 b 돌고 c 돌고 가 아니고 
# a랑 b 돌고 b랑 c 돌고 이런 식으로 b가 두 번 돌게 됨 

def left(temp,x,y):
    tl=copy.deepcopy(temp)
    if x>1 and temp[2*(x-1)]!=temp[2*(x-1)-1]: # 톱니바퀴의 왼쪽 비교 
        if y==1:
            #queue[x-1].rotate(1)
            queue[x-2].rotate(-1)
        else:
            #queue[x-1].rotate(-1)
            queue[x-2].rotate(1)
        left(tl,x-1,-1*y)

def right(temp,x,y):
    tr=copy.deepcopy(temp)
    if x<4 and temp[2*(x-1)+1]!=temp[2*(x-1)+2]: # 톱니바퀴의 오른쪽 비교 
        if y==1:
            #queue[x-1].rotate(1)
            queue[x].rotate(-1)
        else:
            #queue[x-1].rotate(-1)
            queue[x].rotate(1)
        right(tr,x+1,-1*y)

for change in changes: 
    temp=["", a[2], b[-2], b[2], c[-2], c[2], d[-2], ""]
    queue[change[0]-1].rotate(change[1])
    left(temp, change[0],change[1])
    right(temp, change[0],change[1])
    

#print(queue)

answer=0
if queue[0][0]=='1':
    answer+=1
if queue[1][0]=='1':
    answer+=2
if queue[2][0]=='1':
    answer+=4
if queue[3][0]=='1':
    answer+=8

print(answer)
