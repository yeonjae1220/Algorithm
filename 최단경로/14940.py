"""
14940의 Docstring
2 좌표 값 위치 찾아서 그거 기준으로 bfs 돌리면 될듯
"""
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def find_goal():
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                return (i, j)

def bfs(i, j):
    q = deque()
    q.append((i, j, 0))
    visited[i][j] = True
    graph[i][j] = 0

    while q:
        y, x, d = q.popleft()
        for idx in range(4):
            ny = y + dy[idx]
            nx = x + dx[idx]

            if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and graph[ny][nx] != 0:
                q.append((ny, nx, d + 1))
                visited[ny][nx] = True
                graph[ny][nx] = d + 1
                
def unreachable():
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j] != 0:
                graph[i][j] = -1

goal_y, goal_x = find_goal()
bfs(goal_y, goal_x)
unreachable()
for i in range(n):
    for j in range(m):
        print(graph[i][j], end=" ")
    print()

    
