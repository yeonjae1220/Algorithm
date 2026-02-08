# 2 > 4 > 1 > 6 > 3 > 5
#      > 7
# 1 이 root
# 1
# 4 6
# 2 7 / 3
# 5

import sys
from collections import deque

N = int(sys.stdin.readline())
tree = {}

for i in range(1, N + 1):
    tree[i] = []

for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

parents = [0] * (N + 1)
seen = set()
queue = deque([1])
while queue:
    now = queue.popleft()
    seen.add(now)
    for child in tree[now]:
        if child not in seen:
            parents[child] = now
            queue.append(child)

for i in range(2, N + 1):
    print(parents[i])

