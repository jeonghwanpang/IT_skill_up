#백준 1264번 모음의 개수

#idea
#while input=='#'으로 반복문을 돌리고 문자열을 받아서 비교한다.

while True:
    answer=0
    str=input()
    if str=='#':break
    for i in str:
        if i == 'a' or i == 'A':answer+=1
        elif i == 'e' or i == 'E': answer += 1
        elif i == 'i' or i == 'I': answer += 1
        elif i == 'o' or i == 'O': answer += 1
        elif i == 'u' or i == 'U': answer += 1
    print(answer)