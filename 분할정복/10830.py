import sys
n, b = map(int, sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        a[i][j] %= 1000


def div_con(a, b):
    if b == 1:
        return a
    temp = div_con(a, b // 2)
    if b % 2 == 0:
        return mul(temp, temp)
    else:
        return mul(mul(temp, temp), a)
    
def mul(a, b):
    result = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += a[i][k] * b[k][j]
            result[i][j] %= 1000
    return result

result = div_con(a, b)
for i in range(n):
    print(" ".join(map(str, result[i])))

