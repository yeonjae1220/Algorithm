import sys
from collections import deque 
input = sys.stdin.readline

N, M = map(int, input().split())

maze = [list(map(int, input().strip())) for _ in range(M)]

checked = [[N + M] * N for _ in range(M)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

ans = N + M

def bfs():
    global ans
    queue = deque([(0, 0, 0)])
    checked[0][0] = 0
    while queue:
        x, y, walls = queue.popleft()
        if x == N - 1 and y == M - 1:
            ans = min(ans, walls)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                new_walls = walls
                if maze[nx][ny] == 1:
                    new_walls = walls + 1
                
                if checked[nx][ny] > new_walls:
                    checked[nx][ny] = new_walls
                    queue.append((nx, ny, new_walls))


bfs()
print(checked[M-1][N-1])
                
                    
                    
                    





# visited안쓰는 bfs는 무한루프인데 흠
# dp 처럼 각 위치까지 최소한의 벽뚫로 갈 수 있는 데이터 넣으면서 bfs돌릴때마다 얘보다 커지면 갱신 이런 느낌으로?
# 현재 위치의 상하좌우에서 가장 작은값에 현재 위치가 벽이면 + 1, 아니면 최소값?