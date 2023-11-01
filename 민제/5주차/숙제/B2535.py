# 백준 2535 아시아 정보올림피아드

# idea
# 입력 배열의 [3]인덱스를 기준으로 정렬한다.
# 한 국가의 두 개씩 체크하여 소속 국가와 학생 번호를 출력한다.

arr = []
count = 0

for _ in range(int(input())):
    arr.append(list(map(int, input().split())))
check = [0 for i in range(arr[-1][0] + 1)]

arr.sort(key=lambda x: x[2], reverse=True)

for i in arr:
    if check[i[0]] == 2: continue
    print(i[0],i[1])
    count+=1
    check[i[0]] += 1
    if count == 3:
        break
