# 백준 1912번 연속합

# idea
# 각 항에서 max(바로 이전 항까지의 최대값, 자신의 항)으로 찾는다

n = int(input())
arr = list(map(int,input().split()))

d = [0 for i in range(n)]
max_value = -1001

for i in range(n):
    d[i] = max(d[i-1]+arr[i], arr[i])

print(max(d))