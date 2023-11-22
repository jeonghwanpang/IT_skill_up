n = int(input())
arr = list(map(int, input().split()))
dp = [0] * (n+1)

for i in range(1, n+1):
    dp[i] = max(arr[i-1], dp[i-1]+arr[i])

print(max(dp))