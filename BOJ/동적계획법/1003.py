"""
1003의 Docstring

2 0:1 1:1
3 2, 1  0:1 1:2
4 3 2   0:2 1:3
5 4 3   0:3 1:5
6 5 4   0:5 1:8

fib(n-1), fib(n) 출력

"""



import sys
input = sys.stdin.readline

T = int(input())



def fib(n):
    global cnt_0
    global cnt_1
    if dp[n] != -1:
        return dp[n]
    else:
        dp[n] = fib(n-1) + fib(n-2)    
        return dp[n]
        


for _ in range(T):
    n = int(input())
    dp = [-1] * (41) # N 최대 값 + 1
    dp[0] = 0
    dp[1] = 1
    fib(n)
    if n == 0:
        print(1, 0)
    elif n == 1:
        print(0, 1)
    else:
        print(dp[n-1], dp[n])


