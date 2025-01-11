l = int(input())
s = input().rstrip()
hash = 0
for i in range(l):
    hash += (ord(s[i]) - ord('a') + 1) * (31 ** i)
print(hash % 1234567891)