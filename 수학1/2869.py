# a, b, v = map(int, input().split())
# d = 0
# cur = 0
# while(True):
#     d += 1
#     cur += a
#     if cur >= v:
#         print(d)
#         break
#     cur -= b


a, b, v = map(int, input().split())
# (v - a)가 딱 나눠떨어지지 않으면 하루 더 필요
d = (v - a + (a - b - 1)) // (a - b) + 1
print(d)