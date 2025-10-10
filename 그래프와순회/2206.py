import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())

board = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)]for _ in range(N)] 

def bfs():
    queue = deque([(0, 0, 0, 0)]) # x, y, wall_break, distance
    while queue:
        x, y, wall_break, distance = queue.popleft()
        if x == N - 1 and y == M - 1:
            return distance + 1
        for nx, ny in ([x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]):
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == 0 and visited[nx][ny][wall_break] == 0:
                    visited[nx][ny][wall_break] = 1
                    queue.append((nx, ny, wall_break, distance + 1))
                elif board[nx][ny] == 1 and wall_break == 0:
                    visited[nx][ny][wall_break + 1] = 1
                    queue.append((nx, ny, wall_break + 1, distance + 1))

    return -1        



print(bfs())

