import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6) # 👈 이 줄을 추가 (n의 최댓값보다 넉넉하게)

n, m = map(int, input().split())

parents = [0] * (n + 1)
for i in range(n + 1):
    parents[i] = i


def find_parent(x):
    if parents[x] == x:
        return parents[x]
    
    else:
        parents[x] = find_parent(parents[x])
        return parents[x]
    

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b



for _ in range(m):
    cal, a, b = map(int, input().split())
    a = find_parent(a)
    b = find_parent(b)
    if cal == 0:
        if a == b:
            continue
        else:
            union_parent(a, b)
    else:
        if a == b:
            print("YES")
        else:
            print("NO")
