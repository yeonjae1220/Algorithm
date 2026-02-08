num_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

N, B = input().split()
sum = 0
for i, num in enumerate(N[::-1]):
    sum += int(B) ** i * num_list.index(num)
print(sum)

