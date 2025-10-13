import sys
from collections import deque

V = int(sys.stdin.readline())
tree = {}
for i in range(1, V + 1):
    tree[i] = []

for _ in range(V):
    info = list(map(int, sys.stdin.readline().split()))
    node = info[0]
    for i in range(1, len(info) - 2, 2):
        tree[node].append((info[i], info[i+1]))

# 1. brute force : 모든 노드에 대해 dfs or bfs 돌려서 지름 찾기

# 2. 트리의 지름은 랜덤한 노드에서 가장 멀리떨어진 노드와 그 노드에서 가장 멀리 떨어진 노드 사이의 거리
        
def bfs(start_node):
    visited = [False] * (V + 1)
    queue = deque()
    queue.append((start_node, 0))
    visited[start_node] = True
    
    ans = 0
    farthest = 0
    
    while queue:
        curr_node, curr_dist = queue.popleft()
        
        if curr_dist > ans:
            ans = curr_dist
            farthest = curr_node
            
        for next_node, next_dist in tree[curr_node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append((next_node, next_dist + curr_dist))

        
    return ans, farthest


answer = 0
_, farthest = bfs(1)


print(bfs(farthest)[0])

