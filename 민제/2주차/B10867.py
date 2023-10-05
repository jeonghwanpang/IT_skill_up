#백준 10867번 중복 빼고 정렬하기

#idea
#수열을 set으로 받은 뒤 list로 형변환을 해주고 정렬하여 출력한다.

import sys

int(input())
print(' '.join(map(str,sorted(list(set(map(int,sys.stdin.readline().split())))))))