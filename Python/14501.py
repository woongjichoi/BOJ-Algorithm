# DP였음
# DP[i]는 i번째 날까지 일을 했을 때 최댓값
# 뒤에서부터 해주기
# 이해가 될듯 말듯.. 

import sys
input=sys.stdin.readline

n=int(input())
schedule=[]
for i in range(n):
    schedule.append(list(map(int, input().split())))

# [[3,10],[5,20],[1,10],[1,20],[2,15],[4,40],[2,200]]

dp=[0]*(n+1)

for i in range(n-1,-1,-1): 
    temp=i+schedule[i][0]
    if temp>n:
        dp[i]=dp[i+1]
    else:
        dp[i]=max(dp[i+1],schedule[i][1]+dp[temp])
    #print(dp)

print(dp[0])
