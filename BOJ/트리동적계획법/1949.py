# 인접한 노드면 x
# 그러나 우수 마을이 아닌 노드의 이웃 중 적어도 하나는 우수 마을 이어야 함
# 우수 마을의 값 총합이 최대

# n이 우수 마을 일 때 n의 자식 과 부모는 우수 마을 x
# n이 우수 마을 아닐 때 부모 혹은 자식 중 최소 하나는 우수

# DFS로 하면서 비교 하면 되지 않을까
# 노드가 우수일 때, 우수가 아닐 때 담을 배열
# 우수일 때 연결된 노드들의 우수가 아닌 값의 최대 값 + 자신
# 우수가 아닐 때 연결된 노드들 중 우수인 값

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
population = list(map(int, input().split()))

graph = [[] for _ in range(N + 1)]

for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dp = [[0] * 2 for _ in range(N + 1)]
visited = [False] * (N + 1)

def dfs(cur):
    visited[cur] = True
    dp[cur][0] = population[cur - 1]
    dp[cur][1] = 0
    for neighbor in graph[cur]:
        if visited[neighbor]:
            continue
        if not visited[neighbor]:
            dfs(neighbor)
            dp[cur][0] += dp[neighbor][1]
            dp[cur][1] += max(dp[neighbor][0], dp[neighbor][1])


dfs(1)
print(max(dp[1][0], dp[1][1]))

