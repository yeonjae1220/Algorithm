str1 = input()
str2 = input()

len1 = len(str1)
len2 = len(str2)

# DP 테이블 초기화 (0으로 채워진 2차원 리스트)
# 인덱스를 1부터 시작하기 위해 크기를 len+1로 설정
dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

# DP 테이블 채우기
for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        # Case 1: 두 문자가 같은 경우
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        # Case 2: 두 문자가 다른 경우
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# 테이블의 가장 마지막 값이 최종 LCS의 길이
print(dp[len1][len2])