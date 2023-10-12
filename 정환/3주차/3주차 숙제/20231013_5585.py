import sys
input = sys.stdin.readline

a = int(input())
res = 1000 - a
coin = [500,100,50,10,5,1]
count = 0

for i in coin:
    count+=res//i
    res%=i

print(count)
