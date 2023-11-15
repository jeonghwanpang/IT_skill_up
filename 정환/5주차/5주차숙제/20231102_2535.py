n = int(input())
list1= []
count = 0

for _ in range(n):
   list1.append(list(map(int,input().split())))

list1.sort(key=lambda x : -x[2])  #내림차순 람다식 정렬

print (list1[0][0], list1[0][1])
print (list1[1][0], list1[1][1])

if list1[0][0] == list1[1][0]:
   count += 1

for i in range(2, n):
   if count == 0:
      print(list1[i][0], list1[i][1])
   
   else:
        if list1[1][0] != list1[i][0]:
            print(list1[i][0], list1[i][1])
            break