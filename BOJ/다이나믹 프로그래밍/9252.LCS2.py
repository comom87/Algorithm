# 참고: https://velog.io/@emplam27/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EA%B7%B8%EB%A6%BC%EC%9C%BC%EB%A1%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-LCS-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-Longest-Common-Substring%EC%99%80-Longest-Common-Subsequence
# 1
# import sys
# input = sys.stdin.readline

# str1 = input().rstrip()
# str2 = input().rstrip()
# dp = [['' for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
# for i in range(1, len(str1) + 1):
#     for j in range(1, len(str2) + 1):
#         if str1[i - 1] == str2[j - 1]:
#             dp[i][j] = dp[i - 1][j - 1] + str1[i - 1]
#         else:
#             if len(dp[i - 1][j]) > len(dp[i][j - 1]):
#                 dp[i][j] = dp[i - 1][j]
#             else:
#                 dp[i][j] = dp[i][j - 1]
# print(len(dp[-1][-1]))
# print(dp[-1][-1])



# 2
import sys
input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()
dp = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
print(dp[-1][-1])

lcs = ''
x, y = len(str1), len(str2)
while x > 0 and y > 0:
    if dp[x][y] == dp[x - 1][y]:
        x -= 1
    elif dp[x][y] == dp[x][y - 1]:
        y -= 1
    elif dp[x][y] == dp[x - 1][y - 1] + 1:
        x -= 1
        y -= 1
        lcs += str1[x]
if len(lcs) > 0:
    print(lcs[::-1])