a1, a2 = map(int, input().split())
c = int(input())
n = int(input())
fn = a1 * n + a2
gn = n * c
if fn <= gn and a1 > c:
    print(1)
else:
    print(0)