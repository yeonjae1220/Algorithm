"""
시간 초과
"""

# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())

# # 개수별로 1차원 dp 돌아가면서 개수별로 하나 넣을 때, 2개 넣을 떄 .. 쭉쭉 계산하면 되지 않을까? 코인 넣는것 처럼
# # 아니다 2차원 dp로 두고 개수별 차등 적용 해서 더해나가는게 좋을듯

# stuff = []

# for _ in range(N):
#     x, y, z = map(int, input().split())
#     stuff.append((x, y, z))

# dp = [[0] * (M + 1) for _ in range(N + 1)]

# for i in range(1, N + 1):
#     for j in range(1, M + 1):
#         V, C, K = stuff[i - 1]
#         for k in range(1, K + 1):
#             v = V * k
#             c = C * k
#             if v <= j and v <= M:
#                 dp[i][j] = max(dp[i][j], dp[i-1][j], dp[i-1][j-v] + c)
#             else:
#                 dp[i][j] = max(dp[i][j], dp[i-1][j])

# print(dp[N][M])


import sys
input = sys.stdin.readline

N, M = map(int, input().split())

stuff = []

for _ in range(N):
    x, y, z = map(int, input().split())

    idx = 1
    while z > 0:
        temp = min(idx, z)

        stuff.append((x * temp, y * temp))

        z -= temp
        idx *= 2
    
dp = [0] * (M + 1)

for v, c in stuff:
    for m in range(M, v-1, -1):
        dp[m] = max(dp[m], dp[m-v] + c)

print(dp[M])


# 2진수 분해 (Binary Decomposition)
# 예: K=13 -> 1, 2, 4, 6개짜리 묶음으로 나눔
# 이게 핵심, 이거 안쓰고 그냥 k 개수별 전부다 반복문으로 체크하니 시간 초과 뜸

# 1차원 배열을 쓸 때는 무거운 무게부터 역순으로 채워야
# 물건을 중복해서 사용하는 것을 방지할 수 있음.

# 코인 dp 문제 처럼 여러개 되는건 일반 순서대로 하면 여러개 중복 사용 가능
# 이것도 2차원 배열 쓰면 일반 dp처럼 돌릴 수 있을듯
