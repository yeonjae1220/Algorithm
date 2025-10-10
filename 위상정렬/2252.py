import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

graph = {}
for i in range(1, N + 1):
    graph[i] = []

depth = [0 for _ in range(N + 1)]

queue = deque()
ans = []

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    depth[b] += 1


for i in range(1, N + 1):
    if depth[i] == 0:
        queue.append(i)

while queue:
    temp = queue.popleft()
    ans.append(temp)
    for i in graph[temp]:
        depth[i] -= 1
        if depth[i] == 0:
            queue.append(i)

print(*ans)

