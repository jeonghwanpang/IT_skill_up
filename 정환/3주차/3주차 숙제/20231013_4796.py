i = 0

list1 = []
while True:
    i += 1
    l,p,v = map(int,input().split())
    if l  == 0 and p == 0 and v== 0:
        break

    a = v//p    
    b = v % p


    if l < b:
        b = l
   
    result = a * l + b
    list1.append(result)

for k in range(len(list1)):
    print("Case %d: %d" %(k+1 , list1[k] ) )