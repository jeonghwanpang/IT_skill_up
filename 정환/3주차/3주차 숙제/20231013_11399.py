n = int(input())
list1 = list(map(int,input().split()))
list1.sort()

result = 0
for i in range(1, n +1):
    result += sum(list1[:i])

print(result)