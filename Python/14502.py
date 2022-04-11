import sys
input=sys.stdin.readline

import copy
from itertools import combinations

n,m=map(int,input().split())
lab=[list(map(int, input().split())) for _ in range(n)]

empty=[]
virus=[]
for i in range(n):
    for j in range(m):
        if lab[i][j]==0:
            empty.append([i,j])
        elif lab[i][j]==2:
            virus.append([i,j])

directions=[[0,1],[0,-1],[1,0],[-1,0]]

answer=0

def dfs(p,q): # 큐 말고 재귀로 구현 (dfs 안에 dfs가 있는 형태로)
    first_lab[p][q]=2
    for direction in directions:
        x=p+direction[0]
        y=q+direction[1]
        if x<0 or x>=n or y<0 or y>=m:
            continue
        if first_lab[x][y]==0:
            dfs(x,y)
    return
                    

for a,b,c in combinations(empty,3):
    first_lab=copy.deepcopy(lab) # first_lab=lab도 좋은데 깊은 복사 
    first_lab[a[0]][a[1]]=1
    first_lab[b[0]][b[1]]=1
    first_lab[c[0]][c[1]]=1
    
    for v in virus:
        dfs(v[0],v[1])
        
    temp=0
    for i in range(n):
        for j in range(m):
            if first_lab[i][j]==0:
                temp+=1
    answer=max(answer,temp)
    # 백트래킹 대신 깊은 복사 

print(answer)
