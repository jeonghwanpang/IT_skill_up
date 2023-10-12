a = int(input())
list1 = []

for i in range(a):
    b = int(input())

    if b != 0:
        list1.append(b)
    
    else:
        if b == 0:
            list1.pop()
result = sum(list1)
print(result)




    
 