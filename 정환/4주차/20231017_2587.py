list1 =[]
median = 0
idx = 0
for i in range(5):
    n = int(input())

    list1.append(n)
    
result = sum(list1)//5
list1.sort()

print(result)
print(list1[2])

    