#백준 4158번 CD

# idea
# set 자료구조를 통해 중복을 제거해주고 제거된 수를 계산하여 출력한다.

import sys

input = sys.stdin.readline
while True:
    n,m = map(int,input().split())
    if n==0 and m==0:break
    d1 = []
    for i in range(n+m):
        d1.append(int(input()))
    print(n+m-len(set(d1)))