# 먼가 너무 복잡하고 엉망진창으로 풀어놨는데? max 계산을 반복하고 싶지 않아서 이렇게 했는데, 결국 거기서 거기인 코드에
# 복잡하기만 코드가 되버렸네

import sys
input = sys.stdin.readline
TEST_CASE_NUM = 10

# 한 건물 기준으로 좌우 2칸씩 있으면 count
# 크기 3 의 큐 만들어서 쭉 돌리면서 좌우 깎아 가기..?
# 아니면 크기 5 큐만등어서, max 관리 하면서 현재 빌딩과 max 비교..?
# 암튼 주변 기준으로 봤을 때, 현재 건물이 Max가 아니면 조밍권 확보 x

# 계속 비교하는건 좀 아닌듯
# 하나씩 넣어가면서, 이전꺼 보다 큰지 작은지 비교로..
# 이전 꺼 보다 클 때 그냥 큐에 추가 
# 이전 꺼 보다 작을 때  
# 입력 값과 함께 답 적는 배열도 쭉 해놓고 수정해가는게 좋을 듯..?



for test_case_num in range(TEST_CASE_NUM):
    N = int(input())
    building = list(map(int, input().split()))
    ans = [0] * N
    now_max = 0

    for i in range(2, N-2):
        now_max = max(building[i-1], building[i-2])
        if building[i] >= now_max:
            ans[i] = building[i] - now_max
            now_max = building[i]
            ans[i-1] = 0
            ans[i-2] = 0

        else:
            ans[i] = 0
            # 이전 2건물보다 작을 떄 
            if ans[i-1] != 0:
                temp = building[i-1] - building[i]
                if ans[i-1] > temp and temp > 0:
                    ans[i-1] = temp

            if ans[i-2] != 0:
                temp = building[i-2] - building[i]
                if ans[i-2] > temp and temp > 0:
                    ans[i-2] = temp


    print(f"#{test_case_num + 1}", end=" ")
    sum = 0
    for i in range(N):
        sum += ans[i]
    print(sum)

        
        

# enumerate 써서 인덱스랑 같이 받아오면 다루기 쉽나?
# max를 담아두고, 입력 받으며 max가 변화가 생기면 i-2, i-1은 일단 0
##
