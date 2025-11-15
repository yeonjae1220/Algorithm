# 얼리 어답터가 아닌 사람은 친구들이 모두 얼리 어답터일 때 받아들임
# 모든 사람이 얼리 어답터가 되기 위한 최소 수
# 부모와 자식이 전부 얼리 어답터여야 함
# 부모부터 얘가 얼리 어답터일 때 와 아닐 때 나눠서 dp로 쭉 돌려서 visited 로 끝까지 가면 될듯?

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
dp = [[0] * 2 for _ in range(N + 1)]

for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(cur):
    visited[cur] = True
    dp[cur][0] = 1 # 얼리어답터
    dp[cur][1] = 0 # 얼리어답터 x

    for neighbor in graph[cur]:
        if visited[neighbor]:
            continue
        if not visited[neighbor]:
            dfs(neighbor)
            dp[cur][0] += min(dp[neighbor][1], dp[neighbor][0]) # 얼리어답터여도 되고 아니여도 됨
            dp[cur][1] += dp[neighbor][0] # 반드시 얼리어답터가 이웃 노드여야 함

dfs(1)
print(min(dp[1][0], dp[1][1]))
            
