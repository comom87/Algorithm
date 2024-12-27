vowel = ['a', 'e', 'i', 'o', 'u']

while True:
    password = input().rstrip()
    if password == 'end':
        break

    flag = False
    for p in password:
        if p in vowel:
            flag = True
            break
    
    for i in range(len(password) - 2):
        if password[i] in vowel and password[i + 1] in vowel and password[i + 2] in vowel:
            flag = False
            break
        elif password[i] not in vowel and password[i + 1] not in vowel and password[i + 2] not in vowel:
            flag = False
            break

    for i in range(len(password) - 1):
        if password[i] == password[i + 1] == 'e' or password[i] == password[i + 1] == 'o':
            flag = True
        elif password[i] == password[i + 1]:
            flag = False
            break
    
    if flag:
        print(f'<{password}> is acceptable.')
    else:
        print(f'<{password}> is not acceptable.')