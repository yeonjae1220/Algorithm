import sys
input = sys.stdin.readline

N, M = map(int, input().split())

ary = list(map(int, input().split()))
ary.sort()

def bt(arr):
    if len(arr) == M:
        result.append(" ".join(map(str, arr)))
        return
    
    prev = -1
    for i in range(N):
        if visited[i] or prev == ary[i]:
            continue
        
        prev = ary[i]
        arr.append(ary[i])
        visited[i] = True
        bt(arr)
        arr.pop()
        visited[i] = False

result = []
visited = [False] * N
bt([])
for temp in result:
    print(temp)
        