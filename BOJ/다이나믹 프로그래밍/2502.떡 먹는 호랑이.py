# 1
# d, k = map(int, input().split())
# for i in range(k - 1, 0, -1):
#     dp = [0] * d
#     dp[0] = k
#     dp[1] = i
#     flag = True
#     for j in range(2, d):
#         dp[j] = dp[j - 2] - dp[j - 1]

#         if dp[j] > dp[j - 1]:
#             flag = False
#             break
    
#     if flag and dp[-1] >= 1:
#         break
# print(dp[-1])
# print(dp[-2])

# 2
# 참고: https://coooco.tistory.com/50
d, k = map(int, input().split())
dp_a = [0] * (d + 1)
dp_b = [0] * (d + 1)
dp_a[1] = 1
dp_b[2] = 1
for i in range(3, d + 1):
    dp_a[i] = dp_a[i - 2] + dp_a[i - 1]
    dp_b[i] = dp_b[i - 2] + dp_b[i - 1]

for i in range(1, k + 1):
    if (k - dp_a[d] * i) % dp_b[d] == 0:
        print(i)
        print((k - dp_a[d] * i) // dp_b[d])
        break