# 이것도 지름 구하듯 하면 되나..?

import sys
from collections import deque

n = int(sys.stdin.readline())

tree = {}
for i in range(1, n + 1):
    tree[i] = []

for _ in range(n - 1):
    u, v, w = map(int, sys.stdin.readline().split())
    tree[u].append((v, w))
    tree[v].append((u, w))



def bfs(start_node):
    maximum = 0
    farthest_node = start_node # 여기를 0 이 아닌 start_node로 해줘야 만약 더 먼 노드가 없을 때 자기 자신 (거리0)가 될 수 있음
    visited = [False] * (n + 1)
    visited[start_node] = True
    queue = deque([(start_node, 0)]) 
    while queue:
        node, w = queue.popleft()
        if w > maximum:
            farthest_node = node
            maximum = w
        for child, weight in tree[node]:
            if not visited[child]:
                queue.append((child, w + weight))
                visited[child] = True

    return farthest_node, maximum


farthest_node, _ = bfs(1)

print(bfs(farthest_node)[1])

        
            


