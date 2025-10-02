import sys
sys.setrecursionlimit(10**6) # 재귀 깊이를 100만으로 설정

N, M, R = map(int, input().split())

edges = [[] for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, input().split())
    edges[x].append(y)
    edges[y].append(x)

visited = [0] * (N + 1)


count = 1

def dfs(r):
    global count
    visited[r] = count
    count += 1
    edges[r].sort()
    for i in edges[r]:
        if visited[i] == 0:
            dfs(i)

dfs(1)
for i in range(1, N+1):
    print(visited[i])


    