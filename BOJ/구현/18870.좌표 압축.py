# 좌표 압축
# 참고: https://velog.io/@christer10/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%A2%8C%ED%91%9C-%EC%95%95%EC%B6%95

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
compressedNums = sorted(set(nums))
coordinateCompressedNums = {compressedNums[i]: i for i in range(len(compressedNums))}
for num in nums:
    print(coordinateCompressedNums[num], end=' ')