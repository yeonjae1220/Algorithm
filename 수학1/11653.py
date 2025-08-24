import math

n = int(input())
i = 2

while ( i <= math.sqrt(n) ):
    if ( n % i == 0 ):
        n = n // i
        print(i)
    else:
        i += 1

if(n > 1):
    print(n)