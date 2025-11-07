import sys
import heapq
input = sys.stdin.readline
INF = 1e8

N = int(input())
M = int(input())

bus_route = [[] for _ in range(N + 1)] # 1번 노트부터 시작할꺼임

cost = [INF] * (N + 1)

for _ in range(M):
    u, v, w = map(int, input().split())
    bus_route[u].append((v, w))


start, destination = map(int, input().split())


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    cost[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)

        if cost[now] < dist:
            continue

        for i in bus_route[now]:
            if dist+i[1] < cost[i[0]]:
                cost[i[0]] = dist+i[1]
                heapq.heappush(queue, (dist+i[1], i[0]))


dijkstra(start)
print(cost[destination])



