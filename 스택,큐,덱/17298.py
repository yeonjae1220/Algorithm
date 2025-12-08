import sys
input = sys.stdin.readline

N = int(input().strip())

query = list(map(int, input().split()))
stack = []
ans_list = [-1] * N

for i, n in enumerate(query):
    if not stack:
        stack.append((i, n))
    elif stack[-1][1] >= n:
        stack.append((i, n))
    else:
        while stack:
            if stack[-1][1] < n:
                ans_list[stack[-1][0]] = n
                stack.pop()
            else:
                break
        stack.append((i, n))

print(*ans_list)
