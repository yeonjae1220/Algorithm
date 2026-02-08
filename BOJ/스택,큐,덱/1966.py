import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    doc = list(map(int, input().split()))
    q = deque()
    for i in range(N):
        q.append((doc[i], i))

    doc.sort(reverse="True")

    import_idx = 0
    while True:
        now, idx = q.popleft()
        if now < doc[import_idx]:
            q.append((now, idx))
        else:
            if idx == M:
                print(import_idx + 1)
                break
            else:
                import_idx += 1
    





