import sys
input = sys.stdin.readline

n, m = map(int, input().split())
roads = list(map(int, input().split()))
dirty_roads = set()
for _ in range(m):
    ordeals = list(map(int, input().split()))
    if ordeals[0] == 0:
        flip_cnt = len(dirty_roads)
        for dirty_road in list(dirty_roads):
            if dirty_road > 0 and roads[dirty_road - 1] == roads[dirty_road]:
                flip_cnt -= 1
        print(flip_cnt)
    else:
        roads[ordeals[1] - 1] = 1
        dirty_roads.add(ordeals[1] - 1)
