for i in range(3):
    s = input().rstrip()
    if s.isdigit():
        answer = int(s) + 3 - i

if answer % 3 == 0 and answer % 5 == 0:
    print('FizzBuzz')
elif answer % 3 == 0:
    print('Fizz')
elif answer % 5 == 0:
    print('Buzz')
else:
    print(answer)