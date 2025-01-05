words = []
max_length = 0
for _ in range(5):
    word = input().rstrip()
    words.append(word)
    max_length = max(max_length, len(word))

s = ''
for j in range(max_length):
    for i in range(5):
        if len(words[i]) < j + 1:
            continue
        s += words[i][j]
print(s)