n = int(input())
p = 1000000007
# dp = [0] * (n + 1)
dp = {0:0, 1:1, 2:1}


def fibonacci(n):
    if n in dp:
        return dp[n]
    else:
        k = n // 2
        if n % 2 == 0:
            a = fibonacci(k)
            b = fibonacci(k - 1)
            # dp[n] = (a**2 + b**2) % p
            dp[n] = (a + b * 2)*a % p
        else:
            a = fibonacci(k + 1)
            b = fibonacci(k)
            dp[n] = (a**2 + b**2) % p
        
        return dp[n]
    

print(fibonacci(n))




# k = n/2라 가정할 때
# fn = fn/2 * fn/2 + fn/2-1 * fn/2-1