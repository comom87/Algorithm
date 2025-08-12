t = int(input())
for test_case in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    total_arr = [[] for _ in range(n)]

    print(f'#{test_case + 1}')
    for _ in range(3):
        new_arr = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                new_arr[j][n - i - 1] = arr[i][j]
    
        for i in range(n):
            total_arr[i].append(''.join(map(str, new_arr[i])))
    
        arr = new_arr
    
    for row in total_arr:
        print(' '.join(row))
