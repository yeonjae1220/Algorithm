import sys
input = sys.stdin.readline

N, M = map(int, input().split())
quary = sorted(list(map(int, input().split())))

ans = []


def backtracking(arr, depth):
    global ans

    if depth == M:
        ans.append(arr[:])
        return
    
    for q in quary:
        if q not in arr:
            arr.append(q)
            backtracking(arr, depth + 1)
            arr.pop()
    
backtracking([], 0)

for a in ans:
    print(*a)

