# 자음 모음 개수별 구분?
# 모음 cnt 쓰기?
# 모음 cnt 써서 백트레킹 돌리는게 정배 인듯?


import sys
input = sys.stdin.readline

L, C = map(int, input().split())
alpha = input().split()
alpha.sort()


temp = ['a', 'e', 'i', 'o', 'u']


def check(arr):
    a_count, b_count = 0, 0
    for c in arr:
        if c in temp:
            a_count+=1
        else:
            b_count+=1
        
    if a_count >= 1 and b_count>=2:
        return True
    else:
        return False



def backtracking(arr):
    if len(arr) == L:
        if check(arr):
            print("".join(arr))
            return
    for c in range(len(arr), C):
        if arr[-1] < alpha[c]:
            arr.append(alpha[c])
            backtracking(arr)
            arr.pop()


for i in range(C - L + 1):
    a = [alpha[i]]
    backtracking(a)

