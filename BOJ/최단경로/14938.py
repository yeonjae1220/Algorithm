# 이건 다익스트라 쓰는걸 알아서 푼 느낌인데

import sys
import heapq
input = sys.stdin.readline
INF = float('inf')

n, m, r = map(int, input().split())

items = [0] + list(map(int, input().split()))

graph = [[] for _ in range(n + 1)]


for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))


def dijkstra(start):
    d = [INF] * (n + 1)
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

ans = 0
for i in range(1, n + 1):
    temp = 0
    item_distence = dijkstra(i)
    for j in range(1, n + 1):
        if item_distence[j] <= m:
            temp += items[j]
    ans = max(ans ,temp)

print(ans)


