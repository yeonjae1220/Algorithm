import sys
import heapq
input = sys.stdin.readline

INF = float('inf')
N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))


def dijkstra(start):
    d = [INF] * (N + 1)
    q = []
    d[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if d[now] < dist:
            continue

        for next, weight in graph[now]:
            cost = dist + weight
            if cost < d[next]:
                d[next] = cost
                heapq.heappush(q, (cost, next))

    return d

for i in range(1, N + 1):
    distence = dijkstra(i)
    for j in range(1, N + 1):
        if distence[j] == INF:
            print(0, end=" ")
        else:
            print(distence[j], end=" ")
    
    print()


