import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    coin = list(map(int, input().split()))
    M = int(input())

    dp = [0] * (M + 1)
    dp[0] = 1

    # for i in range(1, M + 1):
    #     for c in coin:
    #         if i - c >= 0:
    #             dp[i] += (dp[i-c] + 1)

    for c in coin:
        for i in range(c, M + 1):
            dp[i] += dp[i-c]
    
    print(dp[M])