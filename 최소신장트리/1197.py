# from collections import defaultdict
import heapq

import sys
sys.setrecursionlimit(10**6)

V, E = map(int, input().split())
parent = [i for i in range(V + 1)]

def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x]) # 이거 실수 했었음 주의
    return parent[x]

def kruskal():
    edges = []
    weight = 0
    for _ in range(E):
        i, j, k = map(int, input().split())
        edges.append((i, j, k))

    edges.sort(key=lambda x : x[2])
    for a, b, w in edges:
        # if parent[a] != parent[b]: # 여기도 틀렸음
        if find(a) != find(b):
            union(a, b)
            weight += w

    return weight

def prim(start, weight):

    graph = {}
    for i in range(V+1):
        graph[i] = []
    
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
         

    visited = [False] * (V + 1)
    queue = [(weight, start)]
    sum_weight = 0

    while queue: # 간선 개수를 걸어야하나?
        w, n = heapq.heappop(queue)
        if visited[n]: 
            continue
        visited[n] = True
        sum_weight += w
        for u, we in graph[n]:
            heapq.heappush(queue, (we, u))

    return sum_weight


print(prim(1,0))


# print(kruskal())
