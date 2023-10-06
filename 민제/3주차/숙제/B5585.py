#백준 5585번 거스름돈

#idea
#거스름돈을 리스트에 넣고 반복문을 돌려 큰 거스름돈부터 몫연산을 통해 거슬러주고 나머지 연산을 통해 거스름돈 갱신

coin=[500,100,50,10,5,1]

money=1000-int(input())
answer=0

for i in coin:
    answer+=money//i
    money%=i
print(answer)