n = int(input())
list1 = []
point = 0
result  = 0

for i in range(n):
    m = int(input())
    list1.append(m)

list1.sort(reverse = True)
hab = sum(list1[: 42])

for j in range(n):
    if list1[j] >= 250:
        point = 5
        result += point
    
    elif 200<= list1[j] < 250:
        point = 4
        result += point
    
    elif 140 <= list1[j] <200:
        point = 3
        result += point
    
    elif 100 <= list1[j] < 140:
         point = 2
         result += point
    
    elif 60 <= list1[j] <100:
        point = 1
        result += point
    
    else:
        point = 0

       
    
print(hab,result)

