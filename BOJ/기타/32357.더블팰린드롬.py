# n = int(input())
# palindromes = []
# for _ in range(n):
#     string = input()
#     if string[:len(string) // 2] == string[-1:-(len(string) // 2) - 1:-1]:
#         palindromes.append(string)
# print(len(palindromes) * (len(palindromes) - 1))

n = int(input())
palindrome = 0
for _ in range(n):
    string = input()
    if string == string[::-1]:
        palindrome += 1
print(palindrome * (palindrome - 1))