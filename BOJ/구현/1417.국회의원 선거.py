# 와... heap... 생각지도 못했다... 와...(이마 탁!)
# import heapq

# n = int(input())
# dasom = int(input())
# polls = []
# for _ in range(n - 1):
#     heapq.heappush(polls, -int(input()))

# cnt = 0
# if n != 1:
#     while dasom <= -polls[0]:
#         poll = -heapq.heappop(polls)
#         poll -= 1
#         dasom += 1
#         cnt += 1
#         heapq.heappush(polls, -poll)
# print(cnt)

n = int(input())
dasom = int(input())
polls = [int(input()) for _ in range(n - 1)]
polls.sort(reverse=True)

cnt = 0
if n != 1:
    while dasom <= polls[0]:
        polls[0] -= 1
        dasom += 1
        cnt += 1
        polls.sort(reverse=True)
print(cnt)