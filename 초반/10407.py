# n 층이면 2의 2^n-1

import sys
input = sys.stdin.readline

n = int(input())

if n == 1:
    print(2)
else:
    print(1)

# 근데 생각해보면 처음 2 빼곤 1만 나올 수 밖에 없지 않나?
