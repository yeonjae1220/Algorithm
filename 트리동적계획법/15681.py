import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, R, Q = map(int, input().split())

tree = [[i] for i in range(N + 1)]

for _ in range(N - 1):
    U, V = map(int, input().split())
    tree[U].append(V)
    tree[V].append(U)


    
dp = [0] * (N + 1)
visited = [False] * (N + 1)

def dfs(current):
    visited[current] = True
    dp[current] = 1

    for neighbor in tree[current]:
        if not visited[neighbor]:
            dfs(neighbor)
            dp[current] += dp[neighbor]

dfs(R)

for _ in range(Q):
    q = int(input())
    print(dp[q])
