import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())

bus_route = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, w = map(int, input().split())
    bus_route[u].append((v, w))

start, end = map(int, input().split())

route = [0] * (n + 1)

def dijkstra(s, e):
    q = []
    d = [float('inf')] * (n + 1)
    heapq.heappush(q, (0, s))
    d[s] = 0
    while q:
        dist, now = heapq.heappop(q)

        if d[now] < dist:
            continue

        for neighbor, cost in bus_route[now]:
            cost += dist

            if d[neighbor] > cost:
                d[neighbor] = cost
                route[neighbor] = now
                heapq.heappush(q, (cost, neighbor))

    return d[e]

print(dijkstra(start, end))

path = [end]
now = end
while now != start:
    now = route[now]
    path.append(now)

path.reverse()

print(len(path))
# print(''.join(map(str, path)))
print(*path)
