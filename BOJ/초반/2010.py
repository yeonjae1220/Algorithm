import sys
input = sys.stdin.readline

n = int(input())

sum = 0
for i in range(n):
    multi = int(input())
    if i == 0:
        sum += multi
    else:
        sum += (multi - 1)

print(sum)

