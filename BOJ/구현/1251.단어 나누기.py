word = input().rstrip()
recombination_word = []
for i in range(1, len(word)):
    for j in range(i + 1, len(word)):
        first, second, third = word[i - 1:: -1], word[j - 1:i - 1:-1], word[:j - 1:-1]
        recombination_word.append(first + second + third)
recombination_word.sort()
print(recombination_word[0])