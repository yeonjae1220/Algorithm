"""
bfs로 노드 순서대로 넣어보면서 최소 시간?

아니면 목표 노드부터 역순으로?
    graph에 뒤집어서 넣고
    얘 할려면 해야하는것들 걸리는 시간 더하면서 하면 될듯

1 (7)
8 (5, 6)
20 (2)
1 (3)
10 (1)

흠 안풀린다
"""

# import sys
# input = sys.stdin.readline

# def sol(start):
#     ans = con_time[start]
#     q = [start]
#     visited[start] = True

#     while q:
#         node = q.pop()
#         visited[node] = True
#         temp = 0
#         for c in tac_tree[node]:
#             if not visited[c]: 
#                 q.append(c)
#                 temp = max(temp, con_time[c])
#         ans += temp

#     return ans

# T = int(input())


# for _ in range(T):
#     N, K = map(int, input().split())

#     con_time = [0] + list(map(int, input().split()))

#     tac_tree = [[] for _ in range(N+1)]
#     visited = [False] * (N + 1)

#     for _ in range(K):
#         u, v = map(int, input().split())
#         tac_tree[v].append(u)

#     W = int(input())

#     print(sol(W))


"""
위상정렬을 써야함
"""
            
import sys
from collections import deque
input = sys.stdin.readline

def topology_sort():
    N, K = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    
    graph = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)
    dp = [0] * (N + 1)

    for _ in range(K):
        u, v = map(int, input().split())
        graph[u].append(v)
        indegree[v] += 1

    W = int(input())

    q = deque()

    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = time[i]

    while q:
        now = q.popleft()

        for next in graph[now]:
            dp[next] = max(dp[next], dp[now] + time[next])

            indegree[next] -= 1
            if indegree[next] == 0:
                q.append(next)
    
    print(dp[W])



T = int(input())
for _ in range(T):
    topology_sort()