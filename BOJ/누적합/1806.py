"""
1806의 Docstring

부분합이라고 하는데
그냥 left right idx 설정해서 S 보다 크면 left 밀고, 작으면 right 밀면 되는거 아닌가

"""

import sys
input = sys.stdin.readline
INF = float('inf')

N, S = map(int, input().split())
query = list(map(int, input().split()))
sum = [0] * (N + 1)

for i in range(1, N + 1):
    sum[i] = sum[i-1] + query[i - 1]

l = 0
r = 1

ans = INF

# 0 5 6 9 14 24 31 35 44 46 54

while r < N + 1:
    temp = sum[r] - sum[l]

    if temp >= S:
        ans = min(ans, (r - l))
        l += 1
    
    else:
        r += 1
    


if ans == INF:
    print(0)
else:
    print(ans)