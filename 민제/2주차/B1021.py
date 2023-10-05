#백준 1021번 회전하는 큐

#idea
#deque으로 n만큼의 d=deque(i+1 for i in range(n))를 만들고 for문으로 다음 입력값을 차례로 받는다.
#deque의 중간 인덱스를 기준으로 왼쪽에 있으면 2번 연산을 해주고 오른쪽에 있으면 3번 연산을 해준다.
#각 연산을 d[0]이 i가 아닐 때 동안 반복을 해주고 반복하는 동안 1을 더해준다.
#d[0]이 i가 되면 반복을 멈추고 popleft를 해준다.

from collections import deque

n,m=map(int,input().split())
d=deque(i+1 for i in range(n))
answer=0

for i in list(map(int,input().split())):
    if d.index(i)<=len(d)//2:
        while d[0] != i:
            d.append(d.popleft())
            answer+=1
    else:
        while d[0] != i:
            d.appendleft(d.pop())
            answer+=1
    d.popleft()
print(answer)