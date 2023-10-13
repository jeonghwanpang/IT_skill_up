#백준 1758번 알바생 강호

#idea
# arr에 수열을 입력받고 arr.sort(reverse=true)로 내림차순으로 해준다.
# answer=0으로 초기화한다.
# for 수열을 반복하여 temp = arr[i] - i가 음수면 answer+=0 양수면 answer+=temp를 해준다.
# answer 출력

import sys

input = sys.stdin.readline
arr=[]
answer=0

for i in range(int(input())):
    arr.append(int(input()))

arr.sort(reverse=True)

for i in range(len(arr)):
    temp = arr[i] - i
    if temp>0:
        answer+=temp
print(answer)