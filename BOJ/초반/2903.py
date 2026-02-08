
# 1 > 4
# 2 > 4 + 5 = 9
# 3 > 9 + 16 = 25



# 5 > 1089


# 4
# 4 * 4 - 4 + 1
# 9 * 4 - 11 
# 4 + 2 + 2

# n = (last-1) * 4 - (4*n + n)

# ans = 4
# for i in range(1, n + 1):
#    ans = (ans) * 4 - (ans * i + i)

# print(ans)



# 4 + 1
# 8 + 8


# 1 3 1
# 2 5 2 5 2

# 2 2
# 3 3 3 # 1
# 5 5 5 5 5  # 2
# 9 9 9 9 9 9 9 9 9 # 3

n = int(input())

temp = 2
for i in range(n):
    temp = temp * 2 - 1

print(pow(temp, 2))

