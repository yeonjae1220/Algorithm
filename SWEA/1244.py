import sys
input = sys.stdin.readline

def dfs(n):
    global ans
    if n == cnt:
        ans = max(ans, int("".join(num_list)))
        return
    for i in range(l - 1):
        for j in range(i + 1, l):
            num_list[i], num_list[j] = num_list[j], num_list[i]
            if (n, int("".join(num_list))) not in visited:
                dfs(n+1)
                visited.append((n, int("".join(num_list))))
            num_list[j], num_list[i] = num_list[i], num_list[j]
        


T = int(input())

for test_case in range(1, T + 1):
    num, cnt = map(int, input().split())
    num_list = list(str(num))
    l = len(num_list)
    visited = []
    ans = 0

    dfs(0)
    print(f"#{test_case} {ans}")
    

