import sys, heapq

N, E = map(int, sys.stdin.readline().split())
graph = {}
for i in range(1, N + 1):
    graph[i] = []

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start):
    d = [float('INF')] * (N + 1)
    d[start] = 0
    heap = [(0, start)]
    seen = set()
    while heap:
        dist, now = heapq.heappop(heap)
        if now in seen:
            continue
        seen.add(now)
        for child, w in graph[now]:
            if d[now] + w < d[child]:
                d[child] = d[now] + w
                heapq.heappush(heap, (d[child], child))
    return d

V1, V2 = map(int, sys.stdin.readline().split())

ans1 = dijkstra(1)
ans_via1 = dijkstra(V1)
ans_via2 = dijkstra(V2)

result1 = ans1[V1] + ans_via1[V2] + ans_via2[N]
result2 = ans1[V2] + ans_via2[V1] + ans_via1[N]
result = min(result1, result2)
if result >= float('INF'):
    print(-1)
else:
    print(result)
