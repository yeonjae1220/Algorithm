import sys
from collections import deque
input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = {}
for i in range(1, N + 1):
    graph[i] = []

for _ in range(M):
    v, u = map(int, input().split())
    graph[v].append(u)
    graph[u].append(v)


# 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문 조건을 위한 정렬
for i in range(1, N + 1):
    graph[i].sort()


visited = [False] * (N + 1)
ans_dfs = []
def dfs(s):
    visited[s] = True
    ans_dfs.append(s)
    for v in graph[s]:
        if not visited[v]:
            dfs(v)

queue = deque()
ans_bfs = []
def bfs(s):
    queue.append(s)
    visited[s] = True
    while queue:
        temp = queue.popleft()
        ans_bfs.append(temp)
        for v in graph[temp]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True
        


dfs(V)
print(*ans_dfs)
visited = [False] * (N + 1)
bfs(V)
print(*ans_bfs)