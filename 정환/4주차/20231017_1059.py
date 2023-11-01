import sys

a = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))
n = int(sys.stdin.readline())
num.sort()

if n in num:
    print(0)

else:
    c = 0
    d = 0
    for i in num:
        if i < n:
            c = i
        elif i > n and d == 0:
            d = i

    d -= 1
    c += 1

    
    print((n-c)*(d-n+1)+(d-n))

        

         





