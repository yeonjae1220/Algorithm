arr = [-1] * 26

s = input()
for i in range(len(s)):
    idx = ord(s[i]) - ord('a')
    if arr[idx] == -1:
        arr[idx] = i

print(*arr)
    