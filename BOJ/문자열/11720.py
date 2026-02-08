n = int(input())
str = input().strip()
print(sum(int(i) for i in str))  # 각 문자를 정수로 변환하여 합산