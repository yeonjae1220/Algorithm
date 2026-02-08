import sys
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

sum = [0] * (n + 1)

for i in range(1, n + 1):
    sum[i] = (sum[i-1] + arr[i-1]) % m

cnt = 0
remain = [0] * (m)
for i in range(1, n+1):
    remain[sum[i]] += 1
    cnt += (1 if sum[i] == 0 else 0)

for i in range(m):
    if remain[i] > 1:
        cnt += (remain[i] * (remain[i] - 1)) // 2


print(cnt)



# 1 2 3 4 5
# 1 3 6 10 15
# 1 3 1 0 0