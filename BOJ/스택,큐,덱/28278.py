import sys
N = int(sys.stdin.readline())
stack = []
for i in range(N):
    query = sys.stdin.readline().split()
    if query[0] == '1':
        stack.append(query[1])
    elif query[0] == '2':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif query[0] == '3':
        print(len(stack))
    elif query[0] == '4':
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)