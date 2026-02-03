"""
11403의 Docstring

입력 받아서 방향 그래프 만들고
정점 i에 대해 그래프 순회하며 갈수있는곳 만들어둔 2차원 배열에 1로 바꾸기
자기자신은? -> 입력 보니 다른 노드 거쳐서 자기 자신 돌아올 수 있으면 1로 변경

"""

import sys
input = sys.stdin.readline
from collections import deque

N = int(input())

query = [list(map(int, input().split())) for _ in range(N)]
graph = [[] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if query[i][j] == 1:
            graph[i].append(j)


ans = [[0] * N for _ in range(N)]

def check_connected(n):
    is_connnected = [0] * N
    q = deque()
    for g in graph[n]:
        q.append(g)
        is_connnected[g] = 1
    
    while q:
        now = q.popleft()
        for next in graph[now]:
            if is_connnected[next] == 0:
                q.append(next)
                is_connnected[next] = 1
    
    return is_connnected


ans = []
for i in range(N):
    ans.append(check_connected(i))

for r in ans:
    print(*r)