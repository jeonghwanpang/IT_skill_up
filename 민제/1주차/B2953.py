#백준 2953번 나는 요리사다

#idea
#우선 처음에 num=-1을 해준다.
#answer=0
#for i in range:를 해준다음 temp = sum(map(int,input().split())을 해준다.
#if num<temp라면 num=temp를 해준다음 answer=i+1을 해준다.

answer=0
num=-1

for i in range(5):
    temp=sum(map(int,input().split()))
    if num< temp:
        num=temp
        answer=i+1
print(answer,num)