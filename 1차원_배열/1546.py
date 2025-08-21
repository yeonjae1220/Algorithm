N = int(input())
arr = list(map(int, input().split()))

max = max(arr)
sum = 0

for i in range(N):
    sum += arr[i] / max * 100

print(sum / N)