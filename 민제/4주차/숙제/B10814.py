#백준 10814번 나이순 정렬

#idea
#2차원 배열로 입력받아 lambda를 사용하여 정렬해준다.

import sys

arr=[]

for i in range(int(input())):
    arr.append(sys.stdin.readline().rstrip())
arr.sort(key = lambda x:int(x.split()[0]))
for i in arr:
    print(''.join(map(str,i)))