'''
알파벳 배열 생성 해서 관리
단어 개수 길이를 가진 배열에 각 단어의 길이를 저장
가장 긴 것을 가장 큰 숫자 (9) 할당 후 길이 -1 
순차적으로 전부 할당

아니다 그냥 체크된 알파벳이 있으면 그거 전부 검사해서 숫자 (문자열 상태)로 변환
같은 자리 수 라면 개수가 가장 많은 알파벳이 큰 숫자 가져가기

자릿 수 별 알파벳 모아서 처리
'''

import sys
import string
input = sys.stdin.readline

n = int(input())
query = [input().strip() for _ in range(n)]
alphas = {}

for q in query:
    lenght = len(q) - 1
    for c in q:
        if c in alphas:
            alphas[c] += 10 ** lenght
        else:
            alphas[c] = 10 ** lenght
        lenght -= 1



alphas_sort = sorted(alphas.values(), reverse=True)
tmp = 9
result = 0
for c in alphas_sort:
    result += c * tmp
    tmp -= 1

print(result)








# alpha_list = list(string.ascii_uppercase)
# alpha_sum = [[0] * 8] # 수의 최대 길이는 8

# for i in range(n):
#     query = input()
    
#     for i in range(len(query)):
#         alpha_sum[i].append()
        








