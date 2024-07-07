import sys
input = sys.stdin.readline

k, n = map(int, input().split())
LANs = [int(input()) for _ in range(k)]

def check(mid):
    cnt = 0
    for LAN in LANs:
        cnt += LAN // mid
    return cnt >= n

low, high = 1, max(LANs) + 1
while low + 1 < high:
    mid = (low + high) // 2
    if check(mid):
        low = mid
    else:
        high = mid
print(low)