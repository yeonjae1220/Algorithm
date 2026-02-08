import sys
input = sys.stdin.readline

check = [1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1]

query = input()

sum = 0
idx = 0
for i in range(12):
    if query[i] != '*':
        sum += int(query[i]) * check[i]
    else:
        idx = i

# (sum + (x * check[idx])) mod 10 = 10 - query[12]

for i in range(10):
    if (sum + i * check[idx]) % 10 == (10 - int(query[12])) % 10:
        print(i)
        break