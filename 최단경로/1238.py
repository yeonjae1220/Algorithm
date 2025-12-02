import sys
import heapq
input = sys.stdin.readline

N, M, X = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra(s):
    q = []
    d = [float('inf')] * (N + 1)
    heapq.heappush(q, (0, s))
    d[s] = 0

    while q:
        dist, now = heapq.heappop(q)

        if d[now] < dist:
            continue

        for neighbor, cost in graph[now]:
            cost += dist

            if d[neighbor] > cost:
                d[neighbor] = cost
                heapq.heappush(q, (cost, neighbor))
    
    return d

ans = 0
back = dijkstra(X)
for i in range(1, N + 1):
    go = dijkstra(i)
    ans = max(ans, go[X] + back[i])

print(ans)
