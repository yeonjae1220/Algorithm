import sys
n = int(input())

list = []

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    list.append([a, b])

list.sort(key = lambda x: (x[1], x[0]))

for i in list:
    print(i[0], i[1])