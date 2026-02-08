# deque 선언해두고 그냥 [] 에 pop() 써서 틀림
# deque 쓰고 popleft() 써야함

from collections import deque

def solution(n, edge):
    
    graph = [[] for _ in range(n + 1)]
    for u, v in edge:
        graph[u].append(v)
        graph[v].append(u)
    
    depth = [-1] * (n + 1)
    max_depth = 0
    
    q = deque([])
    q.append((0, 1))
    depth[1] = 0
    while q:
        d, now = q.popleft()
        for c in graph[now]:
            if depth[c] == -1:
                depth[c] = d + 1
                max_depth = max(max_depth, d + 1)
                q.append((d+1, c))
    
    answer = depth.count(max_depth)
    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))