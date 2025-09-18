n = int(input())
arr = list(map(int, input().split()))
arr.sort()
sum = 0
plus = 0
for i in range(n):
    plus += arr[i]
    sum += plus
print(sum)