from sys import stdin

n = int(input())
for i in range(n):
    a, b = map(int, stdin.readline().split())
    print(a+b)