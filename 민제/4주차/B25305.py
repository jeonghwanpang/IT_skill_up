#백준 25305번 커트라인

#idea
#n과 k를 받고 arr에 리스트에 넣고 내림차순 정렬해준다

import sys

n,k=map(int,sys.stdin.readline().split())
print(sorted(list(map(int,sys.stdin.readline().split())),reverse=True)[k-1])