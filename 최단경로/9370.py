import sys, heapq

T = int(sys.stdin.readline())
for _ in range(T):
    n, m, t = map(int, sys.stdin.readline().split())
    s, g, h = map(int, sys.stdin.readline().split())

    graph = {}
    for i in range(1, n + 1):
        graph[i] = []

    for _ in range(m):
        a, b, d = map(int, sys.stdin.readline().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

    dest_candidates = []
    for _ in range(t):
        dest_candidates.append(int(sys.stdin.readline()))
    

    def dijkstra(start):
        global n
        d = [float('inf')] * (n + 1)
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
    
    s_list = dijkstra(s)
    g_list = dijkstra(g)
    h_list = dijkstra(h)

    s_to_g = s_list[g]
    s_to_h = s_list[h]
    
    g_to_h = g_list[h]


    min_heap = []

    for d in dest_candidates:
        g_to_d = g_list[d]
        h_to_d = h_list[d]

        s_to_d = s_list[d]

        if s_to_d == float('inf'):
            continue

        temp1 = s_to_g + g_to_h + h_to_d
        temp2 = s_to_h + g_to_h + g_to_d

        temp = min(temp1, temp2)

        if temp != s_to_d:
            continue

        heapq.heappush(min_heap, (d, temp))
            
    ans = []
    while min_heap:
        d, _ = heapq.heappop(min_heap)
        ans.append(d)
    

    print(*sorted(ans))




# 시작 지점에서 목적지 후보들까지의 최단거리
# 그런데 그 최단 경로가 g-h 간선을 반드시 포함하는가?
# g-h 간선을 체크 방법?
# s -> g -> h -> d
# s -> h -> g -> d
# 위 2가지 경우의 수 중 하나
# 목적지 후보의 수가 100개
# s -> g, s -> h 둘의 최단거리 구해두고 
# g -> d, s -> d 까지 최단거리 쭉 뽑아서 비교



