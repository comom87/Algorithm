import sys
input = sys.stdin.readline

def merge_sort(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid + 1, end)
        merge(arr, start, mid, end)

def merge(arr, start, mid, end):
    i = start
    j = mid + 1
    tmp = []

    while i <= mid and j <= end:
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i += 1
        else:
            tmp.append(arr[j])
            j += 1

    while i <= mid:
        tmp.append(arr[i])
        i += 1
    
    while j <= end:
        tmp.append(arr[j])
        j += 1
    
    i = start
    t = 0

    while i <= end:
        arr[i] = tmp[t]
        answer.append(arr[i])
        i += 1
        t += 1

n, k = map(int, input().split())
nums = list(map(int, input().split()))
answer = []
merge_sort(nums, 0, n - 1)

if len(answer) >= k:
    print(answer[k - 1])
else:
    print(-1)