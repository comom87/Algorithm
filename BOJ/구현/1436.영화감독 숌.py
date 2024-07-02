# 진짜 브루트포스네...ㅎ
# While True로 일일이 탐색해도 n < 10000이므로 반복문이 최대 100만번만 돈다.
n = int(input())
order = 1
endNum = 666

while True:
    if order == n:
        print(endNum)
        break

    endNum += 1
    if '666' in str(endNum):
        order += 1