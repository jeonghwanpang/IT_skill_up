#백준 28455 UnionMapleStory

#idea
# answer배열을 [0,0]으로 만들어준다.
# 레벨을 리스트에 넣어주고 answer[0]에 더해준다.
# 구간별로 능력치를 산정하여 answer[1]에 더해준다.

n=int(input())
arr=[]
level=[250,200,140,100,60]
answer=[0,0]

for i in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)
for i in range(len(arr)):
    if i==42:break
    answer[0]+=arr[i]
    for j in range(len(level)):
        if arr[i]>=level[j]:
            answer[1]+=5-j
            break
print(answer[0], answer[1])