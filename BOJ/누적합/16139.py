# import sys
# S = sys.stdin.readline()
# q = int(sys.stdin.readline())

# alphabet = "abcdefghijklmnopqrstuvwxyz"
# alpha_dict = {}
# for i in range(26):
#     alpha_dict[alphabet[i]] = []

# sum = [alpha_dict] * (len(S))

# for i in range(len(S)):
    


# for _ in range(q):
#     a, l, r = sys.stdin.readline().split()




import sys

input = sys.stdin.readline
S = input().strip()
q = int(input())

counts = {chr(ord('a') + i): [0] * (len(S) + 1) for i in range(26)} # 여기 왜 + 1?

for i in range(len(S)):
    current_char = S[i]
    for j in range(26):
        counts[chr(ord('a') + j)] = counts[chr(ord('a') + j)][i]

    counts[current_char][i+1] += 1

results = []
for _ in range(q):
    a, l, r = sys.stdin.readline().split()
    l = int(l)
    r = int(r)

    result = counts[a][r+1] - counts[a][l]
    results.append(str(result))


print('\n'.join(results))