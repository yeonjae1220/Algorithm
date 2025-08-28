import sys
n = int(sys.stdin.readline())
user = []

for i in range(n):
    a, s = sys.stdin.readline().split()
    user.append([int(a), s, i])

user.sort(key = lambda x : (x[0], x[1]))

for i in user:
    print(i[0], i[1])