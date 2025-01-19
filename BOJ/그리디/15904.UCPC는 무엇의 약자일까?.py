s = input().rstrip()
ucpc = 'UCPC'
i = 0
for w in s:
    if w == ucpc[i]:
        i += 1
    
    if i == 4:
        break

if i == 4:
    print('I love UCPC')
else:
    print('I hate UCPC')