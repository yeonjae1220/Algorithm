# 페르마의 소정리에 따라 a의 역원은 a^(p-2)와 같습니다.
# a^(-1) ≡ a^(p-2) (mod p)

import sys

# 입력을 빠르게 받기 위함
input = sys.stdin.readline

n, k = map(int, input().split())
# 모듈러 연산을 수행할 소수
p = 1000000007

# a^b % p 를 계산하는 함수 (분할 정복 이용)
def power(a, b, m):
    result = 1
    a %= m
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % m
        a = (a * a) % m
        b //= 2
    return result

# 팩토리얼을 미리 계산 (모듈러 연산 적용)
factorial = [1] * (n + 1)
for i in range(2, n + 1):
    factorial[i] = (factorial[i - 1] * i) % p

# 분자 N = n!
numerator = factorial[n]

# 분모 D = k! * (n-k)!
denominator = (factorial[k] * factorial[n - k]) % p

# 분모의 역원을 페르마의 소정리를 이용해 구함
# D^(p-2) % p
denominator_inverse = power(denominator, p - 2, p)

# 최종 결과: (분자 * 분모의 역원) % p
result = (numerator * denominator_inverse) % p

print(result)