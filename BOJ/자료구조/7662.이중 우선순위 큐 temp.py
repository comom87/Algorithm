import sys
import heapq
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    min_heap = []
    max_heap = []
    k = int(input())
    nums = {}
    for _ in range(k):
        command, num = input().split()
        num = int(num)
        if command == 'I':
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            if num not in nums:
                nums[num] = 0
            nums[num] += 1
        elif command == 'D':
            if max_heap and num == 1:
                max_num = -heapq.heappop(max_heap)
                if max_num in nums:
                    nums[max_num] -= 1
            elif min_heap and num == -1:
                min_num = heapq.heappop(min_heap)
                if min_num in nums:
                    nums[min_num] -= 1
        
        heap = []
        for key, value in nums.items():
            for _ in range(value):
                heap.append(key)
        
        min_heap = heap
        max_heap = [-num for num in heap]
        heapq.heapify(min_heap)
        heapq.heapify(max_heap)

    if min_heap:
        print(-heapq.heappop(max_heap), heapq.heappop(min_heap))
    else:
        print('EMPTY')