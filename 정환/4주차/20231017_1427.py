import sys
list1 = list(map(int,sys.stdin.readline().rstrip()))
list1.sort(reverse = True)
list2 = ''.join(str(s) for s in list1)
print(list2)