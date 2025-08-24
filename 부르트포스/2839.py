n = int(input())
cnt = 0
temp = n // 5
for i in range(temp, -1, -1):
    if (n - 5 * i) % 3 == 0:
        cnt = i + (n - 5 * i) // 3
        n = 0
        break
if n == 0:
    print(cnt)
else:
    print(-1)
