import sys
input = sys.stdin.readline

def devide_conquer(fold):
    if len(fold) == 1:
        return True
    
    mid = len(fold) // 2
    for i in range(mid):
        if fold[i] == fold[-1 - i]:
            return False
    
    left = devide_conquer(fold[:mid])
    right = devide_conquer(fold[mid + 1:])
    return left and right

t = int(input())
for _ in range(t):
    fold = list(map(int, input().rstrip()))
    is_fold = devide_conquer(fold)

    if is_fold:
        print('YES')
    else:
        print('NO')