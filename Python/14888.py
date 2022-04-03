import sys
input=sys.stdin.readline

n=int(input())
numbers=list(map(int,input().split()))
operators=list(map(int,input().split()))

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def multiply(x,y):
    return x*y

def division(x,y):
    if x<0 and y>0:
        return (x*(-1)//y)*(-1)
    return x//y

functions=[add, sub, multiply, division]

min_value=1000000000
max_value=1000000000*(-1)

def backtracking(count, number):
    if count==n:
        global max_value, min_value
        max_value=max(max_value,number)
        min_value=min(min_value,number)
        return
    for i in range(4):
        if operators[i]>0:
            operators[i]-=1
            backtracking(count+1, functions[i](number,numbers[count]))
            operators[i]+=1

backtracking(1, numbers[0])
print(max_value)
print(min_value)
