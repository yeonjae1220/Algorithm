import sys
input = sys.stdin.readline

N = int(input())
cows = []
for _ in range(N):
    s, e = map(int, input().split())
    cows.append((s,e))

cows.sort()
temp_end_time = 0

for s, e in cows:
    if s >= temp_end_time:
        temp_end_time = s + e
    else:
        temp_end_time += e

print(temp_end_time)


