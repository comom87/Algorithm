import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    sizes = [0] + list(map(int, input().split()))
    
    prefixSum = sizes[:]
    for i in range(1, k + 1):
        prefixSum[i] += prefixSum[i - 1]

    dp = [[1e9 for _ in range(k)] for _ in range(k)]

    for i in range(k):
        dp[i][i] = 0

    for length in range(1, k):
        for i in range(k - length):
            for j in range(i, i + length):
                dp[i][i + length] = min(dp[i][i + length], dp[i][j] + dp[j + 1][i + length] + (prefixSum[i + length + 1] - prefixSum[i]))
    print(dp[0][-1])