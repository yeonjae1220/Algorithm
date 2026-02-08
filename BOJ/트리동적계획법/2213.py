import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
weight = list(map(int, input().split())) # index 0 부터 시작함

graph = [[] for _ in range(n + 1)]
dp = [[0] * 2 for _ in range(n + 1)]
visited = [False] * (n + 1)
subset = [[[], []] for _ in range(n + 1)]

for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)  


def dfs(cur):
    dp[cur][0] = weight[cur - 1]
    dp[cur][1] = 0
    subset[cur][0] = [cur]
    subset[cur][1] = []
    visited[cur] = True
    for neighbor in graph[cur]:
        if visited[neighbor]:
            continue
        dfs(neighbor)
        dp[cur][0] += dp[neighbor][1]
        subset[cur][0].extend(subset[neighbor][1])

        if dp[neighbor][1] < dp[neighbor][0]:
            dp[cur][1] += dp[neighbor][0]
            subset[cur][1].extend(subset[neighbor][0])
        else:
            dp[cur][1] += dp[neighbor][1]
            subset[cur][1].extend(subset[neighbor][1])
        
dfs(1)

if dp[1][0] < dp[1][1]:
    print(dp[1][1])
    print(*sorted(subset[1][1]))
    
else:
    print(dp[1][0])
    print(*sorted(subset[1][0]))


    



# 부모와 자식이 해당 안될 떄 의 노드 부분집합 최대 찾아야 함
# Dp[][2] 로 적용 될 때랑 안될 때 분리해서 dp 방식으로 쌓아올라가기 
# 재귀로 결국 dp[1][0] dp[1][1] 중 max 찾으면 될 듯?