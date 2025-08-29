import sys
n = int(sys.stdin.readline())
list_a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
list_b = list(map(int, sys.stdin.readline().split()))
dict = {}
for i in range(n):
    dict[list_a[i]] = 0

for i in range(m):
    if list_b[i] not in dict:
        print(0, end = " ")
    else:
        print(1, end = " ")