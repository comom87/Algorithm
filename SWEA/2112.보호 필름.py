def dfs(cnt, index):
    global min_cnt

    if cnt >= min_cnt:
        return

    is_consecutive = True
    for j in range(w):
        consecutive_cnt = 1
        for i in range(d - 1):
            if film[i + 1][j] == film[i][j]:
                consecutive_cnt += 1
            else:
                consecutive_cnt = 1
            
            if consecutive_cnt >= k:
                break
        
        if consecutive_cnt < k:
            is_consecutive = False
            break
    
    if is_consecutive:
        min_cnt = min(min_cnt, cnt)
        return

    for i in range(index + 1, d):
            origin = film[i]
            film[i] = [0] * w
            dfs(cnt + 1, i)
            film[i] = [1] * w
            dfs(cnt + 1, i)
            film[i] = origin

t = int(input())
for test_case in range(t):
    d, w, k = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(d)]
    min_cnt = 1e9

    dfs(0, - 1)

    print(f'#{test_case + 1} {min_cnt}')
