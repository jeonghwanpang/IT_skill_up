#백준 1059번 좋은 구간

#idea
# answer[0,0]
# n,list,k로 인자를 받는다.
# list를 정렬해준다.
# for i in 0,n까지 반복하여 k가 arr[i]보다 작으면 그 구간을 answer 배열에 넣는다
# A가 k보다 작은 구간에서 B는 k부터 answer[1]-1까지 반복된다.
# A가 k보다 작은 갯수는 k-answer[0]-1(왜냐면 K는 포함되지 않으니까) B의 갯수를 (answer[1]-k)개라고 하고
# 두개를 곱해준다.
# 그리고 A==k인 구간에서는 [k,k]를 포함할 수 없으니 B의 갯수를 answer[1]-k-1하여 위에 더해준다.
# (k-answer[0]-1)*(answer[1]-k)+answer[1]-(k+1)를 프린트해준다.

n=int(input())
arr=list(map(int,input().split()))
k=int(input())
answer=[0,0]
arr.sort()
for i in range(len(arr)):
    if k<arr[i]:
        if i == 0:
            answer[1]=arr[i]
        else:
            answer[0]=arr[i-1]
            answer[1]=arr[i]
        break
    elif k==arr[i]:
        print(0)
        exit()
print((k-answer[0]-1)*(answer[1]-k)+answer[1]-(k+1))