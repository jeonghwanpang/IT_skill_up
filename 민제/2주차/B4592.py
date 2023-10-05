#백준 4592번 중복을 없애자

#idea
#len이 100인 list를 0으로 다 초기화시켜 만들어놓는다.
#input 수들을 한개씩 받아 list[input]이 0이면 출력 후 list[input]=1
#list[input]=1이면 continue

while True:
    arr=list(map(int,input().split()))
    if arr[0]==0:break
    for i in range(1,len(arr)):
        if arr[i]==arr[i-1]:
            if i==1:
                print(arr[i],end=' ')
            continue
        else:
            print(arr[i],end=' ')
    print('$')