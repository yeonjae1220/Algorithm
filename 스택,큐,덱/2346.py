import sys
from collections import deque

n = int(sys.stdin.readline())

q = deque(enumerate(map(int, sys.stdin.readline().split())))
ans = []

while q:
    i, j = q.popleft()
    ans.append(i + 1)

    if j < 0:
        q.rotate(-j)
    else:
        q.rotate(-(j - 1))

# print(' '.join(map(str, ans)))
print(*ans)

