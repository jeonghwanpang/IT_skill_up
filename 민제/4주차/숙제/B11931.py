#백준 11931번 수 정렬하기 4

#list로 받아 sort함수를 이용하여 내림차순으로 정렬해준다.

import sys
input = sys.stdin.readline

arr=[int(input()) for i in range(int(input()))]
print('\n'.join(map(str,sorted(arr,reverse=True))))