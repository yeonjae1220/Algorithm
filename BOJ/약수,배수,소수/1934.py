import sys
input = sys.stdin.readline

T = int(input())
def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

for _ in range(T):
    a, b = map(int, input().split())
    print((a*b) // gcd(a, b))
