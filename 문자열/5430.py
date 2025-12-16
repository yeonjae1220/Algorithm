"""
5430의 Docstring
입력대로 계속 연산하는 것 보다
ac에 대해 몇번 뒤집고, left에서 몇개, right에서 몇개 빠지는지 보고 
최종적인 결과만 연산
스택 쓸 필요도 없이 그냥 ac 순회하면서 돌리기
"""


import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    AC = list(input().strip())
    n = int(input())
    s = input().strip()
    # arr = list(map(int, s.strip('[]').split(',')))
    if n == 0:
        arr = []
    else:
        arr = list(map(int, s[1:-1].split(',')))


    cnt_r = 0
    cnt_lpop = 0
    cnt_rpop = 0
    is_error = False

    for ac in AC:
        if ac == 'R':
            cnt_r += 1
        else:
            if cnt_rpop + cnt_lpop >= n:
                is_error = True
                break
            if cnt_r % 2 == 0:
                cnt_lpop += 1
            else:
                cnt_rpop += 1


    if is_error:
        print('error')
    
    else:
        # arr = arr[cnt_lpop:-cnt_rpop]
        if cnt_rpop == 0:
            arr = arr[cnt_lpop:]
        else:
            arr = arr[cnt_lpop:-cnt_rpop]

        if cnt_r % 2 == 1:
            arr = arr[::-1]
        
        # print(arr)
        print("[" + ",".join(map(str, arr)) + "]")