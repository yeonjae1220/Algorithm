def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(0, n-1):
        idx = i
        for j in range(i+1, n):
            if arr[j] < arr[idx]:
                idx = j
        arr[idx], arr[i] = arr[i], arr[idx]
    return arr

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j+1] = arr[j] # 중요
            j-=1
        arr[j+1] = temp

    return arr

def shell_sort(arr):
    n = len(arr)
    h = n // 2

    while h > 0:
        for i in range(h, n):
            temp = arr[i]
            j = i - h
            while j >= 0 and arr[j] > temp:
                arr[j + h] = arr[j]
                j -= h
            arr[j+h] = temp
        h //= 2
    
    return arr




def sort_by_merge(arr):
    temp_arr = [0] * len(arr)
    merge_sort(arr, temp_arr, 0, len(arr) - 1)
    return arr

def merge_sort(arr, temp_arr, left, right):
    if left < right:
        # m = left + (left + right) // 2
        m = (left + right) // 2
        merge_sort(arr, temp_arr, left, m)
        merge_sort(arr, temp_arr, m+1, right)
        merge(arr, temp_arr, left, m , right)

def merge(arr, temp_arr, left, m, right):
    for i in range(left, right + 1):
        temp_arr[i] = arr[i]
    
    part1 = left
    part2 = m + 1 # 
    idx = left

    while part1 <= m and part2 <= right:
        if temp_arr[part1] <= temp_arr[part2]:
            arr[idx] = temp_arr[part1]
            part1 += 1
        else:
            arr[idx] = temp_arr[part2]
            part2 += 1
        idx += 1

    # 굳이 part1 part2 각각 while 안돌려도 됨
    # 우측 부분배열이 다 들어가고 좌측 부분배열만 남은 경우에는 좌측 부분 배열만 넣으면 됨.
    # 좌측 부분배열이 다 들어가고 우측 부분배열만 남은 경우에는 이미 배열은 다 정렬된 것.
    for i in range(m - part1 + 1):
        arr[idx + i] = temp_arr[part1 + i]



# heapsort

def sort_by_quick(arr):
    quick_sort(arr, 0, len(arr) - 1)
    return arr

def quick_sort(arr, left, right):
    part = partision(arr, left, right)
    if left < part - 1:
        quick_sort(arr, left, part - 1)

    if part < right:
        quick_sort(arr, part, right)


def partision(arr, left, right):
    pivot = arr[(left + right) // 2]
    while left <= right:
        while arr[left] < pivot:
            left += 1

        while arr[right] > pivot:
            right -= 1

        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return left














sample_list = [27, -5, 11, 42, 0, 11, 3, -10, 28, 9]

# result = bubble_sort(sample_list)
# result = selection_sort(sample_list)
# result = insertion_sort(sample_list)
# result = shell_sort(sample_list)
# result = sort_by_merge(sample_list)
result = sort_by_quick(sample_list)
print(*result)



