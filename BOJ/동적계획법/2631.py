"""
2631의 Docstring
음? 그냥 선택정렬 하면 되는건가 -> 맨 앞이 아니고 맨 뒤로 보내버리니 수가 달라진다?
와 어케 푸나 했네, dp 안본지 너무 오래됬나보다 이게 생각이 안났네
"""


# import sys
# input = sys.stdin.readline

# N = int(input())

# queue = []
# for _ in range(N):
#     queue.append(int(input()))

# ans = 0

# for i in range(N - 1):
#     if queue[i] == i + 1:
#         continue
#     for j in range(i + 1, N):
#         if queue[j] == i + 1:
#             queue[i], queue[j] = queue[j], queue[i]
#             ans += 1
#             continue

# print(ans)
import sys
input = sys.stdin.readline

N = int(input())

queue = []
for _ in range(N):
    queue.append(int(input()))


dp = [1] * N

for i in range(1, N):
    for j in range(i + 1):
        if queue[i] > queue[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))