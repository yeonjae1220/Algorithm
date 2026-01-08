"""
자기 자신으로 돌아와야함, 최단 경로..라기 보단 A->(웜홀)->B->(도로)->A 이거나 다른 노드를 거쳐서
A까지의 최단거리 기준, 그것보다 높아야 한다..?

시작 지점에서 출발해서 우선 웜홀 찾기?

---
벨만 - 포드 알고리즘 적용

"""

import sys
input = sys.stdin.readline
INF = float("inf")


def bellmanFord():
    global N, M, W

    dist = [0] * (N + 1)

    for i in range(N):
        for cur, nxt, cost in edges:
            if dist[nxt] > dist[cur] + cost:
                dist[nxt] = dist[cur] + cost
                if i == N - 1:
                    return True
    return False


TC = int(input())

for _ in range(TC):
    N, M, W = map(int, input().split())

    # distence = [INF] * (N + 1)
    edges = []

    for _ in range(M):
        S, E, T = map(int, input().split())
        edges.append((S, E, T))
        edges.append((E, S, T))

    for _ in range(W):
        S, E, T = map(int, input().split())
        edges.append((S, E, -T))

    

    if bellmanFord():
        print("YES")
    else:
        print("NO")
        
        