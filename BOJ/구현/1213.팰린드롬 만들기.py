import sys
input = sys.stdin.readline

name = input().rstrip()
length = len(name)
alphabet = {}
for letter in name:
    if letter not in alphabet:
        alphabet[letter] = 0
    alphabet[letter] += 1

odd_alphabet = []
for key, value in alphabet.items():
    if value % 2 == 1:
        odd_alphabet.append(key)

if len(odd_alphabet) > 1:
    print("I'm Sorry Hansoo")
else:
    palindrome = ''
    for key, value in sorted(alphabet.items()):
        palindrome += key * (value // 2)
    
    if odd_alphabet:
        palindrome += odd_alphabet[0] + palindrome[::-1]
    else:
        palindrome += palindrome[::-1]
        
    print(palindrome)
