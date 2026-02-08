"""
10942의 Docstring

할때마다 슬라이싱 [::-1] 로 비교?

"""

# import sys
# input = sys.stdin.readline

# N = int(input())
# query = list(map(int, input().split()))

# M = int(input())

# for _ in range(M):
#     S, E = map(int, input().split())
#     if query[S-1:E] == query[S-1:E][::-1]:
#         print(1)
#     else:
#         print(0)


import sys
input = sys.stdin.readline

N = int(input())
query = list(map(int, input().split()))

dp = [[0] * N for _ in range(N)]

for i in range(N):
    dp[i][i] = 1

for i in range(N-1):
    if query[i] == query[i+1]:
        dp[i][i+1] = 1

for length in range(3, N + 1):
    for i in range(N - length + 1):
        j = i + length - 1
        if query[i] == query[j] and dp[i+1][j-1]:
            dp[i][j] = 1

M = int(input())
for _ in range(M):
    S, E = map(int, input().split())
    print(dp[S - 1][E - 1])