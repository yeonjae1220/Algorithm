import sys
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

sum = [0] * (n + 1)

for i in range(n + 1):
    if i == 0:
        sum[i] = 0
    else:
        sum[i] = sum[i-1] + arr[i-1]


for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(sum[b] - sum[a - 1])



# import sys
# n, m = map(int, sys.stdin.readline().split())
# arr = list(map(int, sys.stdin.readline().split()))

# sum = [[0 for _ in range(n)] for _ in range(n)]


# sum[0][0] = arr[0]
# for i in range(n):
#     for j in range(i+1):
#         if i==j:
#             sum[i][j] = arr[i]
#         else:
#             sum[i][j] = sum[i-1][j] + arr[i]

# for i in range(m):
#     a, b = map(int, sys.stdin.readline().split())
#     print(sum[b-1][a-1])

