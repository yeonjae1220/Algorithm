"""
BOJ.동적계획법.14501의 Docstring

가치랑 소요 시간 같이 dp에 넣어야겠는데
해당 일자 넣을 때 안넣을 때 2개로?

"""
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [0 for _ in range(N + 1)]

for i in range(N):
    for j in range(i + arr[i][0], N + 1):
        if dp[j] < dp[i] + arr[i][1]:
            dp[j] = dp[i] + arr[i][1]

print(dp[-1])



