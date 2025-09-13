import sys
n, m = map(int, input().split())
list_a = list(map(int, sys.stdin.readline().split()))
list_b = list(map(int, sys.stdin.readline().split()))
dict = {}
for i in range(n):
    dict[list_a[i]] = i

cnt = 0
for i in range(m):
    if list_b[i] in dict:
        cnt += 1

print(n + m - cnt*2)
