import sys
input = sys.stdin.readline

s = input().rstrip()
substring = set()
for length in range(1, len(s) + 1):
    for i in range(len(s) - length + 1):
        substring.add(s[i:i + length])
print(len(substring))