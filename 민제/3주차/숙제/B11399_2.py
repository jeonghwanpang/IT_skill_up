##백준 11399번 ATM

#idea
#수열을 intlist로 받고 내림차순 정렬해준다.
#for를 전체 갯수에서 역순으로 반복해주고 * 수열을 해준다.

n=int(input())
arr=sorted(list(map(int,input().split())),reverse=True)
answer=0

for i in range(n-1,-1,-1):
    answer+=arr[i]*(i+1)
print(answer)