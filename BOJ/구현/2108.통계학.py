import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort()

print(round(sum(nums) / n))
print(nums[n // 2])

numsCnt = defaultdict(int)
for num in nums:
    numsCnt[num] += 1
maxCnt = max(numsCnt.values())
maxCntNum = []
for key, value in numsCnt.items():
    if value == maxCnt:
        maxCntNum.append(key)
maxCntNum.sort()
if len(maxCntNum) == 1:
    print(maxCntNum[0])
else:
    print(maxCntNum[1])
print(nums[-1] - nums[0])