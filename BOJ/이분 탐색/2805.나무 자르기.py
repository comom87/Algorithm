import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

def check(mid):
    lengthSum = 0
    for tree in trees:
        if tree >= mid:
            lengthSum += tree - mid
    return lengthSum >= m

# 체크리스트
# check(low) = T, check(hi) = F를 만족하는가?
# low는 정답이 될 수 있는 모든 범위를 나타낼 수 있는가? -> 1 <= M <= 2,000,000,000이므로 low는 0 ~ max(trees) - 1 가능
low, high = 0, max(trees)
while (low + 1 < high):
    mid = (low + high) // 2
    if check(mid):
        low = mid
    else:
        high = mid
print(low)