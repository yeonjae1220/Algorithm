n = int(input())
arr = []
for i in range (n):
    arr.append(int(input()))


dp = [0] * n

if n >= 1:
    dp[0] = arr[0]
if n >= 2: 
    dp[1] = dp[0] + arr[1]
if n >= 3:
    dp[2] = max(arr[0], arr[1]) + arr[2]
if n >=4:
    for i in range (3, n):
        dp[i] = (max(dp[i-2], dp[i-3] + arr[i-1]) + arr[i])

print(dp[n-1])