import sys
input = sys.stdin.readline

people = int(input())
d = {}

for i in range(people):
    a,b = map(str,input().split())
    
    if b == 'enter':
        d[a] = True
    else:
        del d[a]
    
c = sorted(d, reverse = True)

for a in c:
    print(a)











    
