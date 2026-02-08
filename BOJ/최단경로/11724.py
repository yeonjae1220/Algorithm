import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

graph = [[i] for i in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)



def sol(n):
    if visited[n]:
        return
    else:
        visited[n] = True
        for next in graph[n]:
            sol(next)

ans = 0
for i in range(1, N + 1):
    if not visited[i]:
        sol(i)
        ans += 1
print(ans)
