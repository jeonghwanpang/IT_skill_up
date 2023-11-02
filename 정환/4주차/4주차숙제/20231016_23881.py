#교환 횟수를 알아야한다.. 교환이 이루어 지면 횟수를 1 증가시켜야함..    

import sys

a,b = map(int,sys.stdin.readline().split()) #배열의 크기와 횟수 입력
arr = list(map(int,sys.stdin.readline().split())) #배열의 원소를 받아야함
count = 0

def selection(arr):
    global count
    result =[]

    for i in range(a - 1, 0, -1): #오름차순으로
        max = arr[0]
        index = 0

        for j in range(0, i+1): 
            if arr[j] > max:
                max = arr[j]
                index = j
        
        if i != index:
            arr[i], arr[index] = arr[index], arr[i]
            count += 1
        
        if count == b:
           result.append(arr[index])
           result.append(arr[i])
           return result
        
    result.append(-1)
    return result
        
print(*selection(arr))


