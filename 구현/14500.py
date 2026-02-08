"""
14500의 Docstring

백트래킹 돌려가면서 확인?

정사각형 4개이므로 
dx dy 정해서 depth 4되면 총합 큐에 넣기

중복 제거는? 일단 없이 해보자

"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]



ans = 0

def backtracking(x, y, sum, depth):
    global ans
    if depth == 3:
        ans = max(ans, sum)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx]:
            visited[ny][nx] = True
            backtracking(nx, ny, sum + graph[ny][nx], depth + 1)
            visited[ny][nx] = False


def backtracking_t(x, y, sum, depth):
    global ans
    if depth == 3:
        ans = max(ans, sum)
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx]:
            visited[ny][nx] = True
            backtracking_t(x, y, sum + graph[ny][nx], depth + 1)
            visited[ny][nx] = False

    
for i in range(N):
        for j in range(M):
             visited[i][j] = True
             backtracking(j, i, graph[i][j], 0)
             backtracking_t(j, i, graph[i][j], 0)
             visited[i][j] = False
             




print(ans)