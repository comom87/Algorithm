# 참고: https://hooongs.tistory.com/320

n = int(input())
k = int(input())
dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

for i in range(n + 1):
    dp[i][0] = 1
    dp[i][1] = i

for i in range(2, n + 1):
    for j in range(2, k + 1):
        # i번째 색에서 j개의 색을 선택하는 경우 = i번째 색을 선택하는 경우 + i번째 색을 선택하지 않는 경우
        #                               = (i - 2)번째 색에서 (j - 1)개의 색을 선택하는 경우 + (i - 1)번째 색에서 j개의 색을 선택하는 경우
        dp[i][j] = (dp[i - 2][j - 1] + dp[i - 1][j]) % 1000000003
# 색상환은 원형
# n번째 색에서 k개의 색을 선택하는 경우 = n번째 색을 선택하는 경우(n번째 색을 선택하면 1번째 색은 선택하지 못한다.) + n번째 색을 선택하지 않는 경우
#                               = (n - 3)번째 색에서 (k - 1)개의 색을 선택하는 경우 + (n - 1)번째 색에서 k개의 색을 선택하는 경우
dp[n][k] = (dp[n - 3][k - 1] + dp[n - 1][k]) % 1000000003

print(dp[n][k])