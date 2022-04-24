import sys, copy
input=sys.stdin.readline

n,m=map(int, input().split())
company=[list(map(int, input().split())) for _ in range(n)]
cctv=[]

for i in range(n):
    for j in range(m):
        if company[i][j]==1 or company[i][j]==2 or company[i][j]==3 or company[i][j]==4 or company[i][j]==5:
            cctv.append([company[i][j],i,j])

directions=[
    [],
    [[0],[1],[2],[3]],
    [[0,2],[1,3]],
    [[0,1],[1,2],[2,3],[3,0]],
    [[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
    [[0,1,2,3]]
]

dx=[-1,0,1,0]
dy=[0,-1,0,1]

answer=float("inf")

# directions=[[[0,1],[0,-1],[-1,0],[1,0]],[[0,1,0,-1],[-1,0,1,0]],[[-1,0,0,1],[-1,0,0,-1],[1,0,0,-1],[1,0,0,1]],
#             [[-1,0,0,-1,0,1],[-1,0,0,-1,1,0],[0,-1,1,0,0,1],[1,0,0,1,-1,0]],[[-1,0,1,0,0,-1,0,1]]]

def fill(i,x,y,arr): # i=[0,2]
    for ii in i: # ii=0
        a=x
        b=y
        while True:
            a+=dx[ii]
            b+=dy[ii]
            if a<0 or a>=n or b<0 or b>=m:
                break
            if arr[a][b]==6:
                break
            arr[a][b]="#"

# company 초기화?
def dfs(depth, arr):
    global answer
    temp=copy.deepcopy(arr)
    if depth==len(cctv):
        #print(arr)
        #print("***")
        count=0
        for i in range(n):
            for j in range(m):
                if arr[i][j]==0:
                    count+=1
        answer=min(answer,count)
        return

    cctv_num,x,y=cctv[depth]
    for i in directions[cctv_num]:
        fill(i,x,y,arr)
        dfs(depth+1,arr)
        arr=copy.deepcopy(temp)

dfs(0, company)
print(answer)



