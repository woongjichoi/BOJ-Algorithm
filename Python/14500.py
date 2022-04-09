# 놓친 테트리스 모양들 있었음 https://jeongchul.tistory.com/670

n,m=map(int,input().split())

board=[]
for i in range(n):
    board.append(list(map(int, input().split())))

tetromino = [
    [(0,0), (0,1), (1,0), (1,1)], # ㅁ
    [(0,0), (0,1), (0,2), (0,3)], # ㅡ
    [(0,0), (1,0), (2,0), (3,0)], # ㅣ
    [(0,0), (0,1), (0,2), (1,0)], 
    [(1,0), (1,1), (1,2), (0,2)],
    [(0,0), (1,0), (1,1), (1,2)], # ㄴ
    [(0,0), (0,1), (0,2), (1,2)], # ㄱ
    [(0,0), (1,0), (2,0), (2,1)],
    [(2,0), (2,1), (1,1), (0,1)],
    [(0,0), (0,1), (1,0), (2,0)], 
    [(0,0), (0,1), (1,1), (2,1)],
    [(0,0), (0,1), (0,2), (1,1)], # ㅜ
    [(1,0), (1,1), (1,2), (0,1)], # ㅗ
    [(0,0), (1,0), (2,0), (1,1)], # ㅏ
    [(1,0), (0,1), (1,1), (2,1)], # ㅓ
    [(1,0), (2,0), (0,1), (1,1)],
    [(0,0), (1,0), (1,1), (2,1)],
    [(1,0), (0,1), (1,1), (0,2)],
    [(0,0), (0,1), (1,1), (1,2)]
]

answer=0

def find(i,j):
    global answer
    for k in range(19):
        temp=0
        for l in range(4):
            try:
                x=i+tetromino[k][l][0]
                y=j+tetromino[k][l][1]
                temp+=board[x][y]
            except IndexError:
                continue
        answer=max(temp,answer)
            

for i in range(n):
    for j in range(m):
        find(i,j)

print(answer)
