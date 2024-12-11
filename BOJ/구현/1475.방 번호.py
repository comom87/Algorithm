num = list(map(int, input()))
cnt = [0] * 10
for n in num:
    cnt[n] += 1
cnt[6] = cnt[9] = (cnt[6] + cnt[9] + 1) // 2
print(max(cnt))