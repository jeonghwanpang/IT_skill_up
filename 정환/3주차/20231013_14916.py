# 5로 나누어 떨어질 때는 그냥 나눈값.
# 5의 배수가 아니면 2씩 빼면서 5로 나누어 떨어지게
# 2씩 뺏더니 음수가 되면? 
import sys
input = sys.stdin.readline

a= int(input())
count = 0

while True:
    if a % 5 == 0:
       count += a//5
       break

    else:
        a -= 2
        count += 1

        if a < 0:
           count -= 1

print(count)
