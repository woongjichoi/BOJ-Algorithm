import sys
input=sys.stdin.readline

from itertools import combinations

n,m=map(int, input().split())
city=[list(map(int, input().split())) for _ in range(n)]

# 0: 빈 칸, 1: 집, 2: 치킨 집 
# 도시의 치킨 거리(=모든 집의 치킨 거리의 합)를 min으로 

chickens=[] 
houses=[]
for i in range(n):
    for j in range(n):
        if city[i][j]==2:
            chickens.append([i,j])
        elif city[i][j]==1:
            houses.append([i,j])

answer=10000 # 큰 값으로 초기화 (answer=float("inf")로 초기화해도 됨)

# 집 하나의 치킨 거리를 구해주는 함수 
def chickenDistance(house, comb):
    temp_answer=10000 # 큰 값으로 초기화 (answer=float("inf")로 초기화해도 됨)
    for c in comb:
        temp=abs(house[0]-c[0])+abs(house[1]-c[1])
        temp_answer=min(temp,temp_answer)
    return temp_answer

for comb in combinations(chickens,m): 
    tmp=0
    for house in houses:
        tmp+=chickenDistance(house, comb)
    answer=min(tmp,answer)

print(answer)
        
    
    
