from collections import deque

n, m = map(int, input().split())
q = input().split(' ')
queue = deque([i+1 for i in range(n)])

#for i in range(n):
#  queue.append(i+1)

count = 0
for item in q:
  while True:
    if queue[0] == int(item):
      queue.popleft()
      break
    else:
      if queue.index(int(item)) < len(queue)/2:
        while queue[0] != int(item):
          queue.append(queue.popleft())
          count += 1
      else:
        while queue[0] != int(item):
          queue.appendleft(queue.pop())
          count += 1
      
#print(queue)
print(count)