n = int(input())
nums = list(map(int, input().split()))
num_cnt = [0] * 201
for num in nums:
    num_cnt[num] += 1
v = int(input())
print(num_cnt[v])