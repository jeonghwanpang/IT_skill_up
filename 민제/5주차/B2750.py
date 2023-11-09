from collections import deque

def radixSort(nums):
    buckets = [deque() for _ in range(10)]
    minus_buckets = [deque() for _ in range(10)]

    queue = deque()
    minus_queue = deque()
    for i in nums:
        if i>=0:
            queue.append(i)
        else:
            minus_queue.append(-i)
    if queue and minus_queue:
        max_val = max(max(queue), max(minus_queue))
    elif queue:
        max_val = max(queue)
    elif minus_queue:
        max_val = max(minus_queue)

    digit = 1

    while max_val // digit > 0:
        while minus_queue:
            num = minus_queue.popleft()
            minus_buckets[((num) // digit) % 10].append(num)

        while queue:
            num = queue.popleft()
            buckets[(num // digit) % 10].append(num)

        for bucket in buckets:
            while bucket:
                queue.append(bucket.popleft())
        for bucket in minus_buckets:
            while bucket:
                minus_queue.append(bucket.popleft())
        digit *= 10
    for i in reversed(minus_queue):
        print(-i)
    for i in queue:
        print(i)


data = []
for i in range(int(input())):
    data.append(int(input()))
radixSort(data)
