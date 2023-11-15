# 백준 2579번 계단 오르기

# idea
# 다이나믹 프로그래밍을 사용하여 답을 구한다.
# 연속된 세 개의 계단을 건널 수 없으니 계단이 3개가 넘으면 1,3,4 or 2,4 의 계단 중 하나를 선택해준다.

n = int(input())
answer = [0] * 301
arr = [0]

for _ in range(n):
    arr.append(int(input()))

if n == 1:
    answer[1] = arr[1]
elif n == 2:
    answer[2] = arr[1] + arr[2]
if len(arr) > 3:
    answer[1] = arr[1]
    answer[2] = answer[1] + arr[2]
    answer[3] = max(arr[1] + arr[3], arr[2] + arr[3])
    for i in range(4, n + 1):
        answer[i] = max(answer[i - 3] + arr[i - 1] + arr[i], answer[i - 2] + arr[i])

print(answer[n])
