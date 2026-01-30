"""
2166의 Docstring
신발끈 공식이 있음
"""
import sys
input = sys.stdin.readline

N = int(input())

cal1 = 0
cal2 = 0

list_x = []
list_y = []

for _ in range(N):
    x, y = map(int, input().split())
    list_x.append(x)
    list_y.append(y)

for i in range(N - 1):
    cal1 += list_x[i] * list_y[i + 1]
    cal2 += list_x[i + 1] * list_y[i]

cal1 += list_x[N - 1] * list_y[0]
cal2 += list_x[0] * list_y[N - 1]

ans = abs(cal1 - cal2) / 2
print(f"{ans:.1f}")
# print(round(ans, 1))    