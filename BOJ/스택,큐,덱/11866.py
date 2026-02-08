N, K = map(int, input().split())
arr = []
for i in range(1, N + 1):
    arr.append(i)

result = []
idx = 0
while arr:
    idx += (K - 1)
    if idx >= len(arr):
        idx %= len(arr)
    result.append(arr.pop(idx))

print("<" + ", ".join(map(str, result)) + ">")


