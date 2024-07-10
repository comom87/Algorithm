# 누적 합
# 참고: https://book.acmicpc.net/algorithm/prefix-sum

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
prefixSums = [0]
tempSum = 0
for i in range(n):
    tempSum += nums[i]
    prefixSums.append(tempSum)
for _ in range(m):
    i, j = map(int, input().split())
    print(prefixSums[j] - prefixSums[i - 1])