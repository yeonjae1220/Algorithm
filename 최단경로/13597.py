# 전에 bfs로 푼거 다익스트라로 풀기
# 모든 비용을 1로 해서 목적지까지 최소 비용   
import sys, heapq

N, K = map(int, sys.stdin.readline().split())

def dijkstra(start):
    d = [float('inf')] * (100001)
    queue = [(0, start)]
    d[start] = 0
    seen = set()
    while queue:
        dist, now = heapq.heappop(queue)
        if now == K:
            return dist
            # return d

        if now in seen:
            continue
        seen.add(now)
        
        for child in (now - 1, now + 1):
            if 0 <= child <= 100000:
                if d[now] + 1 < d[child]:
                    d[child] = d[now] + 1
                    heapq.heappush(queue, (d[child], child))

        if 0 <= now * 2 <= 100000:
            if d[now] < d[now * 2]:
                d[now * 2] = d[now]
                heapq.heappush(queue, (d[now * 2], now * 2))
        
print(dijkstra(N))
# print(*dijkstra(N))
        


    
# 4, 1 / 6, 1/ 10, 0
# 3, 2 / 8, 1 // 7, 1 / 12, 1 // 9, 1 / 11, 1 / 20, 0
