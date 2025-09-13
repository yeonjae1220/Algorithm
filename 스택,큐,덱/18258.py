import sys
from collections import deque

n = int(sys.stdin.readline())

queue = deque([])

for i in range(n):
    query = sys.stdin.readline().split()
    if query[0] == "push":
        queue.append(query[1])
    elif query[0] == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif query[0] == "size":
        print(len(queue))
    elif query[0] == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif query[0] == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif query[0] == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])