# 맨 앞뒤 공백 제거 후, 공백 세기
# 그냥 split으로 받아서 리스트나 배열에 넣은 다음 개수 세기

str = input().strip()
if str == "":
    print(0)
else:
    n = str.split(' ')
    print(len(n))

