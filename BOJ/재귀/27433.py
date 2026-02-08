import sys
N = int(sys.stdin.readline())

def fac(n):
    if n == 1 or n == 0:
        return 1
    return n * fac(n-1)

print(fac(N))

