import sys
input = sys.stdin.readline

n = int(input())
encrypted_words = input().split()
for encrypted_word in encrypted_words:
    word = ''
    for i in range(len(encrypted_word) // 2):
        word += chr(((ord(encrypted_word[2 * i]) - ord('a')) + (ord(encrypted_word[2 * i + 1]) - ord('a')) - n) % 26 + ord('a'))
    print(word, end=' ')