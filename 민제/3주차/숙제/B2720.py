#백준 2720번 세탁소 사장 동혁

#idea
#리스트에 25,10,5,1을 넣어놓고 반복문을 돌려 거스름돈에서 리스트를 나눈값을 출력하고 나머지로 갱신한다.

import sys

cent=[25,10,5]
for i in range(int(sys.stdin.readline())):
    money=int(sys.stdin.readline())
    for j in cent:
        print(money//j,end=' ')
        money%=j
    print(money)    