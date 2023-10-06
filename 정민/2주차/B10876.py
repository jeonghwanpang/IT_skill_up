import sys

int(input())
p = map(int, sys.stdin.readline().split())

set1 = set(p)

print(' '.join(map(str, sorted(list(set1)))))
