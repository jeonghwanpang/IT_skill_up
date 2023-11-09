# 백준 2750번 수 정렬하기 (브론즈2)

def radix_sort_positive(arr):
    # 배열이 비어있는 경우, 바로 반환
    if not arr:  
        return arr
    
    # 가장 큰 수의 자릿수를 구합니다.
    max_num = max(arr)
    max_digit = len(str(max_num))

    # 10개의 큐를 생성합니다.
    queues = [[] for _ in range(10)]

    # 자릿수별로 반복하여 정렬합니다.
    for digit in range(max_digit):
        for num in arr:
            # 각 자릿수의 숫자를 가져옵니다.
            digit_num = (num // (10 ** digit)) % 10
            # 해당 숫자를 가진 원소를 큐에 넣습니다.
            queues[digit_num].append(num)

        # 큐에 있는 원소들을 순서대로 꺼내어 배열에 저장합니다.
        arr_idx = 0
        for queue in queues:
            while queue:
                arr[arr_idx] = queue.pop(0)
                arr_idx += 1

    return arr


def radix_sort(arr):
    positives = []
    negatives = []

    for num in arr:
        if num >= 0:
            positives.append(num)
        else:
            negatives.append(-num)

    positives = radix_sort_positive(positives)
    negatives = radix_sort_positive(negatives)

    sorted_arr = []
    for num in reversed(negatives):
        sorted_arr.append(-num)

    for num in positives:
        sorted_arr.append(num)

    return sorted_arr

list1 = []
for _ in range(int(input())):
    list1.append(int(input()))

list2 = radix_sort(list1)
for item in list2:
    print(item)
