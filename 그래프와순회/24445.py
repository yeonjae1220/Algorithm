import sys
from collections import deque
N, M, R = map(int, sys.stdin.readline().split())

visited = [0] * ( N + 1)
c = 1
graph = [[] for _ in range(N+1)]



for i in range(1, M + 1):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1, N+1):
    graph[i].sort(reverse=True)



def bfs(n):
    global c
    visited[n] = c
    c += 1
    queue = deque([n])

    while queue:
        v = queue.popleft()
    
        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = c
                c += 1


bfs(R)

for i in range(1, N+1):
    print(visited[i])