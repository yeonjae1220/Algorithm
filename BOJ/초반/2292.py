n = int(input())

right_bound = 1

p = 1

while True:
    if n <= right_bound:
        print(p)
        break

    right_bound = right_bound + 6 * p
    p += 1