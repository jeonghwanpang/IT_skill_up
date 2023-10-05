#백준 10773번 제로

# idea
# answer_list를 빈리스트로 만들어놓는다.
# for i in range(int(input())으로 반복문을 돌린다.
# 그 안에서 수를 입력받으면 answer_list에 append, 0을 입력받으면 answer_list.pop()

import sys

input = sys.stdin.readline

answer_list=[]

for i in range(int(input())):
    n=int(input())
    if n!=0:
        answer_list.append(n)
    else:
        answer_list.pop()
print(sum(answer_list))
