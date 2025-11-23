import sys
input = sys.stdin.readline

n = int(input())
is_palindrom = 0

for _ in range(n):
    string = input().strip()
    if string == string[::-1]:
        is_palindrom += 1
    
if is_palindrom < 2:
    print(is_palindrom)

else:
    print(is_palindrom * (is_palindrom - 1))