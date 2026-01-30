import sys
import statistics
input = sys.stdin.readline

N = int(input())

num = []
for _ in range(N):
    num.append(int(input()))

num.sort()

# 산술평균
# print(int((sum(num) / N) + 0.5))
print(round(sum(num) / N))

# 중앙값
print(num[int(N//2)])

# 최빈값
temp = statistics.multimode(num)
if len(temp) > 1:
    print(temp[1])
else:
    print(*temp)


# 범위
print(num[-1] - num[0])