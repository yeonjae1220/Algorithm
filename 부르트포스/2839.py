n = int(input())
cnt = 0
temp = n // 5
for i in range(temp, -1, -1):
    if (n - 5 * i) % 3 == 0:
        cnt = i + (n - 5 * i) // 3
        n = 0
        break
if n == 0:
    print(cnt)
else:
    print(-1)


# https://velog.io/@goplanit/Algorithm-%EB%B0%B1%EC%A4%80-2839%EB%B2%88-%EC%84%A4%ED%83%95-%EB%B0%B0%EB%8B%AC%ED%8C%8C%EC%9D%B4%EC%8D%AC
# 이 풀이가 훨 깔끔하네