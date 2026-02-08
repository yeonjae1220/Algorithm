"""
BOJ.최단경로.1219의 Docstring
벨만 포드

d[next] < d[now] + c + d_value[next] 일때 바꿔줌으로써 비용이 큰 곳으로 이동

시작 지점 받고 끝지점 확인
끝 지점이 INF 일 때
끝 지점이 정상 값일 때


=> 사이클에서 END 까지 갈 수 있는지 확인하는 로직이 필요함, d[END] == INF 만이 해결해주지 않음
"""

import sys
from collections import deque
input = sys.stdin.readline
INF = -(float('inf'))

N, START, END, M = map(int, input().split())

edges = []

for _ in range(M):
    u, v, c = map(int, input().split())
    edges.append((u, v, c))
    # edges.append((map(int, input().split())))

value = list(map(int, input().split()))

d = [INF] * (N)
cycle = set()

def bf(start):
    d[start] = value[start]

    for i in range(N):
        for u, v, c in edges:
            if d[u] != INF and d[v] < d[u] - c + value[v]:
                d[v] = d[u] - c + value[v]
                if i == N - 1:
                    cycle.add(v)
            

def check_can_end(start_nodes):
    visited = [False] * N
    q = deque(start_nodes)

    for s in start_nodes:
        visited[s] = True

    while q:
        cur = q.popleft()
        if cur == END:
            return True
        
        for u, v, _ in edges:
            if u == cur and not visited[v]:
                visited[v] = True
                q.append(v)
    
    return False

bf(START)

if d[END] == INF:
    print("gg")
elif check_can_end(cycle):
    print("Gee")
else:
    print(d[END])