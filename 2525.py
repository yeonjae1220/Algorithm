h, m = map(int, input().split())
t = int(input())

a, b = divmod(m+t, 60)

print(((h+a) % 24), b)