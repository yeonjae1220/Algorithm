import sys
s = sys.stdin.readline()

n = len(s)

s_set = set()

for i in range(n):
    for j in range(i+1, n):
        s_set.add(s[i:j])

print(len(s_set))