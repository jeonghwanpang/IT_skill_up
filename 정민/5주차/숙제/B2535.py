n = int(input())
list= []
count = 0

for _ in range(n):
   list.append((map(int,input().split())))

list.sort(key = lambda x: -x[2])  #내림차순 람다식 정렬

print (list[0][0], list[0][1])
print (list[1][0], list[1][1])

if list[0][0] == list[1][0]:
   count += 1

for i in range(2, n):
   if count == 0:
      print(list[i][0], list[i][1])
   
   else:
        if list[1][0] != list[i][0]:
            print(list[i][0], list[i][1])
            break
        
        