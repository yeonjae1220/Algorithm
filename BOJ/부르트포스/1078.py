import sys
input = sys.stdin.readline

N = int(input())
F = int(input())

temp = N // 100
temp *= 100

while temp % F != 0:
    temp += 1

print(str(temp)[-2:])
