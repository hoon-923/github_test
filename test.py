# 주석 추가
import sys
r=sys.stdin.readline
T=int(r())
# 주석 추가 2
dx = [1,-1,0,0]
dy = [0,0,1,-1]
for _ in range(T):
    M,N,K = map(int,r().split())
    field =[[0] * M for _ in range(N)]
    q = []
    worm = 0
    for _ in range(K):
        X,Y = map(int,r().split())
        field[Y][X] = 1
    for y in range(N):
        for x in range(M):
            if field[y][x]:
                q.append((x,y))
                worm += 1
                while q:
                    temp = q[0]
                    q = q[1:]
                    if field[temp[1]][temp[0]]:
                        field[temp[1]][temp[0]] = 0
                        for i in range(4):
                            new_x = temp[0] + dx[i]
                            new_y = temp[1] + dy[i]
                            if 0 <= new_x < M and 0 <= new_y < N and field[new_y][new_x]:
                                q.append((new_x,new_y))
    print(worm)
