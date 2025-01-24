# 참고
# https://afterdawncoding.tistory.com/202
# 아니.... 이게 뭐람... 난이도 실버3 맞아...?

n, m = map(int, input().split())
if n == 1:
    print(1)
elif n == 2:
    print(min((m + 1) // 2, 4))
elif m <= 6:
    print(min(m, 4))
else:
    print(m - 2)