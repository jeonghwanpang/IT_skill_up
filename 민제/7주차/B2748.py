# 백준 2748번 피보나치 2

# idea
# 다이나믹 프로그래밍을 써서 구현

n = int(input())

d = [0,1] + [0 for i in range(n-1)]

for i in range(2,n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])