import sys
a, b, c = map(int, sys.stdin.readline().split())

# print(pow(a, b, mod=c))

def div(a, b, c):
    if b == 1:
        return a % c
    
    temp = div(a, b//2, c)
    
    if b % 2 == 0:
        return (temp ** 2) % c

    else:
        return (temp ** 2 * a) % c


print(div(a, b, c))