n=int(input())
applicant=list(map(int, input().split()))
B,C=map(int, input().split())

answer=0
answer+=len(applicant)
 
for i in range(len(applicant)):
    applicant[i]-=B

for a in applicant:
    if a<0:
        continue
    elif a%C==0:
        answer+=a//C
    else:
        answer+=a//C+1

print(answer)

# applicant의 원소가 음수가 될 수도 있으며
# -1%2==1 이런 식으로 음수도 나머지 계산된다는 것 
