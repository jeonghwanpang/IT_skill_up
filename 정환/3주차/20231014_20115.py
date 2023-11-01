n = int(input())
drink = list(map(int,input().split()))
drink.sort()

hab = drink[-1]

for i in range(n-1):
    hab += drink[i]/2

print(hab)