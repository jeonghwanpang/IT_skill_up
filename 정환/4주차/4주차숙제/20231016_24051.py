def insertion_sort(numbers, val):
    n = len(numbers)
    cnt=0
    num = 0
    for i in range(1, n):
        now = numbers[i]
        j = i - 1
        while j >= 0 and numbers[j] > now:
            numbers[j + 1] = numbers[j]
            cnt+=1
            
            if cnt==val:
                num = numbers[j + 1]            
            j -= 1
        numbers[j + 1] = now
        cnt+=1


        if cnt==val:
            num = numbers[j + 1]   
    if val>cnt:
        return print(-1)
    else:
        return print(num)



A, B = map(int, input().split())
numbers = list(map(int, input().split()))
insertion_sort(numbers, B)