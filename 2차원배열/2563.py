# 하나 받을 때 마다 기존 색종이들과 겹치는 영역 비교 해서 겹치는 영역 빼고 더하기

import sys
N = int(sys.stdin.readline())
papers = [[0] * 101 for _ in range(101)]
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            papers[i][j] = 1

overlap_area = 0
for i in range(101):
    for j in range(101):
        if papers[i][j] == 1:
            overlap_area += 1
print(overlap_area)