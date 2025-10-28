# n은 123456까지 -> 123456*2 까지 검사하면 됨

BOUNDARY = 123456 * 2

check = [True] * (BOUNDARY + 1)

check[0] = False
check[1] = False

for i in range(BOUNDARY + 1):
    if check[i] == False:
        continue
    temp = 2

    while temp * i <= BOUNDARY:
        check[temp*i] = False
        temp += 1



while True:
    n = int(input())
    if n == 0:
        break

    cnt = 0
    for i in range(n + 1, n*2 + 1):
        if check[i]:
            cnt += 1

    print(cnt)


    






