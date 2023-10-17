#백준 2587번 대표값2

#idea
# list를 받아서 정렬후 중값값과 평균 출력

answer=0
arr=[]
for i in range(5):
    n=int(input())
    answer+=n
    arr.append(n)
arr.sort()

print(answer//5)
print(arr[2])