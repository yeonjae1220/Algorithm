"""
1389의 Docstring

그래프로 만들어서 다익스트라? bfs로 찾는게 나을듯
"""

import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

connecion = [[] for _ in range(N + 1)]


for _ in range(M):
    a, b = map(int, input().split())
    if b not in connecion[a]:
        connecion[a].append(b)
        connecion[b].append(a)

visited = [False] * (N + 1)

def bfs(n, depth):
    total = 0
    q = deque()
    q.append((n, 0))
    visited[n] = True

    while q:
        now, depth = q.popleft()
        for next in connecion[now]:
            if not visited[next]:
                q.append((next, depth + 1))
                visited[next] = True
                total += (depth + 1)
    
    return total



ans_list = []
for i in range(1, N + 1):
    visited = [False] * (N + 1)
    ans_list.append(bfs(i, 0))
                
min_val = min(ans_list)

# print(ans_list)
print((ans_list.index(min_val)) + 1) # ans_list 인덱스는 0부터 시작해서 1 더해줘야함



    