#백준 1343번 폴리오미노

#idea
# temp=0으로 초기화, answer=[]로 빈배열을 만들어준다.
# i=0을 해주고 for문으로 문자열을 반복해주며
# 'X'면 temp+=1, 문자열[i+1]='.'이면 answer에 temp만큼 'AAAA'와 'BB'를 담아준다
# i==len(arr-1)이라면 answer에 temp만큼 'AAAA'와 'BB'를 담아준다.
# 'AAAA'와 'BB'를 담아주는 구현은 반복되므로 메소드를 만들어 사용한다.
# 이 메소드에서 temp가 홀수면 -1을 출력해주고 프로그램 종료

answer=[]
s=input()
temp=0

def string_input(temp):
    if temp % 2 == 0:
        answer.append('AAAA' * (temp // 4))
        temp %= 4
        answer.append('BB' * (temp // 2))
        temp %= 2
    else:
        print(-1)
        exit()

for i in range(len(s)):
    if s[i] == 'X':
        temp+=1
        if len(s)-1 != i:
            if s[i+1] == '.':
                string_input(temp)
                temp=0
        else:
            string_input(temp)
            temp=0
    else:
        answer.append('.')
print(''.join(answer))
