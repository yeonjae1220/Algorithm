import sys

n, k = map(int, sys.stdin.readline().split())
arr = [0] * n
for i in range(n):
    arr[i] = int(sys.stdin.readline())

arr = sorted(arr, reverse=True)

cnt = 0
sum = 0

for i in range(n):
    if sum + arr[i] <= k:
        temp = (k - sum) // arr[i]
        cnt += temp
        sum += arr[i] * temp

    if sum == k:
        break

print(cnt)
