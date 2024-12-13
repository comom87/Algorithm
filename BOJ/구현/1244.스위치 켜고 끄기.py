import sys
input = sys.stdin.readline

n = int(input())
switch = [-1] + list(map(int, input().split()))
k = int(input())
for _ in range(k):
    gender, num = map(int, input().split())
    if gender == 1:
        for i in range(num, n + 1, num):
            switch[i] ^= 1
    elif gender == 2:
        switch[num] ^= 1
        for i in range(1, min(num - 1, n - num) + 1):
            if switch[num - i] != switch[num + i]:
                break
            switch[num - i] ^= 1
            switch[num + i] ^= 1

for i in range(1, n + 1):
    print(switch[i], end=' ')
    if i % 20 == 0:
        print()