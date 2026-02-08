import sys
import heapq
V, E = map(int, sys.stdin.readline().split())

start_node = int(sys.stdin.readline())

graph = {}
for i in range(1, V + 1):
    graph[i] = []

for _ in range(E):
    s, e, w = map(int, sys.stdin.readline().split())
    graph[s].append((e, w))

def dijkstra(start):
    global V
    n = len(graph) - 1
    d = [float('inf')] * (V + 1)
    d[start] = 0
    heap = [(0, start)]
    seen = set() # 이미 최단 경로를 확정한 정점(node)을 다시 방문하지 않도록 하여 불필요한 계산을 막고 효율성을 높임
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

ans = dijkstra(start_node)
for i in range(1, V + 1):
    if ans[i] == float('inf'):
        print("INF")
    else:
        print(ans[i])