# 단순히 계산..?
# 아니면 1, 1부터 x, y 까지의 합을 전부 구한다음 잘 뺴보기? -> 이게 맞는거 같은데


import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

dp = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == 0 and j == 0:
            dp[i][j] = graph[i][j]
        
        elif i == 0:
            dp[i][j] = dp[i][j-1] + graph[i][j]
        
        elif j == 0:
            dp[i][j] = dp[i-1][j] + graph[i][j]

        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + graph[i][j]

ans = []

# 이렇게 처리 안하고 그냥 else안에 If 방식으로만 했어도 됬네
for i in range(M):
    y1, x1, y2, x2 = map(int, input().split())
    if x1 == x2 and y1 == y2:
        ans.append(graph[y1-1][x1-1])

    else:
        x1, y1, x2, y2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
        
        if x1 > 0 and y1 > 0:
            ans.append(dp[y2][x2] - dp[y1-1][x2] - dp[y2][x1-1] + dp[y1-1][x1-1])
        elif x1 > 0 and y1 == 0:
            ans.append(dp[y2][x2] - dp[y2][x1-1])
        elif x1 == 0 and y1 > 0:
            ans.append(dp[y2][x2] - dp[y1-1][x2])
        else:
            ans.append(dp[y2][x2])

for a in ans:
    print(a)