import sys

a = int(sys.stdin.readline())

list1 = []

for i in range(a):
    list1.append(int(sys.stdin.readline()))

list1.sort(reverse = True)

result = 0

for i in range(a):
    ans = list1[i] - i
    if ans <0:
        break
    result += list1[i] - i

print(result)

