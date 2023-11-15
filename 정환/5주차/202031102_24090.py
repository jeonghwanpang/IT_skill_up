import sys
sys.setrecursionlimit(int(1e6))
input = sys.stdin.readline

def partition(p, r):
    global k, cnt, nums
    pivot = nums[r]
    i = p-1
    for j in range(p, r):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
            cnt += 1
            if cnt == k:
                if nums[i] <= nums[j]:
                    print(nums[i], nums[j])
                else:
                    print(nums[j], nums[i])
                exit()
    if i+1 != r:
        nums[i+1], nums[r] = nums[r], nums[i+1]
        cnt += 1
        if cnt == k:
            if nums[i+1] <= nums[r]:
                print(nums[i+1], nums[r])
            else:
                print(nums[r], nums[i+1])
            exit()
    return i+1

def quick_sort(p, r):
    if p >= r:    return
    q = partition(p, r)
    quick_sort(p, q-1)
    quick_sort(q+1, r)
    
if __name__ == "__main__":
    global nums
    n, k = map(int, input().strip().split())
    nums = list(map(int, input().strip().split()))
    cnt = 0
    quick_sort(0, len(nums)-1)
    if k > cnt: print(-1)