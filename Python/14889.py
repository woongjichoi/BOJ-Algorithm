# 시간초과 줄이는 것이 관건!! 하나하나 연산 낭비되는 부분 다 찾아서 줄이기 

import sys
input=sys.stdin.readline

n=int(input())
abilities=[]
for i in range(n):
    abilities.append(list(map(int, input().split())))

# [시간 초과] players를 1부터 n+1까지로 하고 sum_start에서 [t[0]-1][t[1]-1] 이런 식으로 하면 시간 초과인데
# players를 0부터 n까지로 하고 sum_start에서 [t[0]][t[1]] 이런 식으로 하면 시간 초과 안 남 
players=[]
for i in range(0,n):
    players.append(i)

answer=1000 # 조금 허접하긴 한데.. min으로 갱신할 거라 큰 수 아무거나 초기화 

# [시간 초과] combinations, permutations 둘 다 import하는 것보다 하나만 import하는 게 나음 
from itertools import combinations

# [시간 초과] for ~ in combinations 할 때 combinations 굳이 list에 안 넣고 돌려도 됨★

for start in combinations(players,n//2):
    # [시간 초과] 두 집단으로 나눌 때 반은 combinations로 고르고 걔네를 방문 처리하고 방문 처리 안 된 애들을 리스트에 담아서 나머지 집단을 골랐는데
    # 그냥 set(전체)-set(combinations로 고른 애들) 하면 바로 됨★
    link=set(players)-set(start)
            
    sum_start=0
    for t in combinations(start,2):
        sum_start+=abilities[t[0]][t[1]]
        sum_start+=abilities[t[1]][t[0]]
    sum_link=0
    for t in combinations(link,2):
        sum_link+=abilities[t[0]][t[1]]
        sum_link+=abilities[t[1]][t[0]]
        
    answer=min(answer,abs(sum_start-sum_link))

print(answer)
