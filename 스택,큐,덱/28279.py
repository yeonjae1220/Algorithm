import sys
from collections import deque

N = int(sys.stdin.readline())
q = deque()
for _ in range(N):
    arr = list(map(int, sys.stdin.readline().split()))

    if arr[0] == 1:
        q.appendleft(arr[1])
    elif arr[0] == 2:
        q.append(arr[1])
    elif arr[0] == 3:
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif arr[0] == 4:
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop())
    elif arr[0] == 5:
        print(len(q))
    elif arr[0] == 6:
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif arr[0] == 7:
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif arr[0] == 8:
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])
    