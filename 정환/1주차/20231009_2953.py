result = []
for i in range(5):
     a = list(map(int,input().split()))
     result.append(sum(a))
print(result.index(max(result)) + 1 , max(result))    