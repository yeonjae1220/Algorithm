import sys
input = sys.stdin.readline

N = int(input())

if N == 0:
    print(0)
    sys.exit()

level = []
for _ in range(N):
    level.append(int(input()))

level.sort()

idx = int(N * 0.15 + 0.5)

level = level[idx:N - idx]

print(int(sum(level) / len(level) + 0.5))