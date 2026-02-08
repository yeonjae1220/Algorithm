import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

dp = [[0] * (sum(C) + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    byte = A[i - 1]
    cost = C[i - 1]
    for j in range(sum(C) + 1):
        if j < cost:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(byte + dp[i-1][j-cost], dp[i-1][j])

for i in range(sum(C) + 1):
    if dp[N][i] >= M:
        print(i)
        break



