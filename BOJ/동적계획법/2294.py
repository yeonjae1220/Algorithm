"""
BOJ.동적계획법.2294의 Docstring

동전들 set으로 종류별로 구하고
dp로 싹싹 돌려가면서 비교해가면 되나?

"""

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))

dp = [100001 for _ in range(k + 1)]
dp[0] = 0

for c in coins:
    for i in range(c, k + 1):
        dp[i] = min(dp[i], dp[i-c] + 1)


if dp[k] == 100001:
    print(-1)
else:
    print(dp[k])



