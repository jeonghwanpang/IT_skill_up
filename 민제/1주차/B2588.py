#백준 2588번 곱셈

#idea
#우선 첫 번째 숫자를 int a에 받고 두 번째 숫자를 int b에 받는다 변수 answer=a*b을 만들어준다..
#a 곱하기 b의 각 자릿수를 곱하고 전체 결과를 출력하면 되는 문제이므로 나머지 연산과 나누기 연산을 사용하여 풀면 된다.
#for i in range(3)으로 반복을 해준 다음 안에서 answer_1=a*(b%10)을 넣어주고
# print(answer_1)로 결과를 출력해준다. 그 다음 b를 b//10으로 초기화해준다.
#여기서 answer_1=a*b_1 print(a*b_1)을 해주고 b=b_2를 해준다. for문의 마지막에는 answer+=answer_1*10^(i-1)을 해준다.

a = int(input())
b = int(input())
answer=a*b

for i in range(3):
    answer_1=a*(b%10)
    print(answer_1)
    b=b//10
print(answer)