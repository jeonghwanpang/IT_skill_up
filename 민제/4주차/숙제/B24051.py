#백준 24051번 알고리즘 수업 - 삽입 정렬 1

#idea
# 삽입정렬을 구현하고 count=0으로 초기화해준다.
# 수가 바뀌는 count해주고 count=k가 되는 순간 저장된 수를 print해주고 exit()해준다.
# 마지막줄에 print(-1)을 해주어 exit()되지 않았으면 -1을 출력해준다.

import sys

n,k = map(int,input().split())
arr=list(map(int,sys.stdin.readline().split()))
count=0

for i in range(1,len(arr)):
    temp=arr[i]
    if arr[i]>arr[i-1]:continue
    for j in range(i,0,-1):
        if temp < arr[j-1]:
            arr[j] = arr[j-1]
            count+=1
        elif temp>arr[j-1]:
            arr[j] = temp
            count+=1
            break
        if count == k:
            print(arr[j])
            exit()
    else:
        arr[0]=temp
        count+=1
print(-1)