"""
그냥 큐에 다 넣고 K번째마다 q.pop() 해서 ans 리스트에 넣으면 끝인가
"""

import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

ans = []
q= deque([i for i in range(1, N+1)])

cnt = 1
while q:
    now = q.popleft()
    if cnt % K == 0:
        ans.append(now)
    else:
        q.append(now)
    cnt += 1

print('<', ', '.join(map(str, ans)), '>', sep='')
