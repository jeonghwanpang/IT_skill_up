#백준 1439번 뒤집기

#idea
#수열에서 0과 1이 연속적으로 배치되어 있는 갯수를 찾아서 더 적은 갯수를 출력한다.
#예시에서 말한 전체를 뒤집는 경우는 고려하지 않아도 된다.

s=list(map(int,input()))
count=[0,0]
prev=s[0]
count[prev]+=1

for i in range(1,len(s)):
    now=s[i]
    if prev != now:
        count[now]+=1
    prev=now
print(min(count))