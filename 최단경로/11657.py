import sys
input = sys.stdin.readline
INF = float('inf')

N, M = map(int, input().split())

edges = []

for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((A, B, C))

dist = [INF] * (N + 1)

def bf(start):
    dist[start] = 0
    for i in range(N):
        for a, b, c in edges:
            if dist[a] != INF and dist[b] > dist[a] + c:
                dist[b] = dist[a] + c
                if i == N - 1:
                    return False
            
    return True

if bf(1):
    for i in range(2, N + 1):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])
else:
    print(-1)

        