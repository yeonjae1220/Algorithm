# left-max, right-max로 최대 넓이 구하면서 max값보다 낮은게 나오면, 
# 낮은값 * 지금까지 진행한거 넓이와 기존 최대 넓이 비교
# 다음께 더 크면 낮은값 * 지금까지 진행 + 1, 더 작으면 위 로직 이용
# left와 right가 만나면 종료

import sys
while True:
    arr = list(map(int, sys.stdin.readline().split()))
    if arr[0] == 0:
        break
    arr = arr[1:]
    stack = []
    max_area = 0
    index = 0
    while index < len(arr):
        if not stack or arr[stack[-1]] <= arr[index]:
            stack.append(index)
            index += 1
        else:
            top = stack.pop()
            if not stack:
                area = arr[top] * index
            else:
                area = arr[top] * (index - stack[-1] - 1)
            max_area = max(area, max_area)
    while stack:
        top = stack.pop()
        if not stack:
            area = arr[top] * index
        else:
            area = arr[top] * (index - stack[-1] - 1)
        max_area = max(area, max_area)
    print(max_area)
