# 1
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
memories = [0] + list(map(int, input().split()))
costs = [0] + list(map(int, input().split()))
dp = [[0 for _ in range(sum(costs) + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(sum(costs) + 1):
        if costs[i] > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - costs[i]] + memories[i])

answer = 1e9
for i in range(sum(costs) + 1):
    if dp[n][i] >= m:
        answer = min(answer, i)
        break
print(answer)



# 2
# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())
# memories = [0] + list(map(int, input().split()))
# costs = [0] + list(map(int, input().split()))
# dp = [[0 for _ in range(sum(costs) + 1)] for _ in range(n + 1)]
# for i in range(1, n + 1):
#     for j in range(sum(costs) + 1):
#         if costs[i] > j:
#             dp[i][j] = dp[i - 1][j]
#         else:
#             dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - costs[i]] + memories[i])

# for i in range(sum(costs) + 1):
#     if dp[n][i] >= m:
#         print(i)
#         break



# 3
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))
length = sum(costs) + 1
dp = [0] * length
for i in range(n):
    # 오름차순인 경우, 이후의 값이 이전의 갱신된 값을 바탕으로 갱신된다.
    for j in range(length - 1, costs[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - costs[i]] + memories[i])

for i in range(length):
    if dp[i] >= m:
        print(i)
        break