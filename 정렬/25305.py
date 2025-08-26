N, k = map(int, input().split())

list = list(map(int, input().split()))

list.sort(reverse=True)

print(list[k-1])
