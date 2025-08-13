'''
    메모리: 70,016KB
    시간: 1,131ms
'''

'''
    아이디어
    - 보호 필름 단면의 모든 세로 방향에 대해서 동일한 특성의 셀들이 k개 이상 연속적으로 있는 경우에만 성능 검사 통과
    - 보호 필름이 성능 검사를 통과하지 못하는 경우 막 별로 약품 투입

    - ⭐시간 복잡도를 고려하여 가지치기를 잘하는 것이 중요⭐
'''

def dfs(cnt, index):
    global min_cnt

    if cnt >= min_cnt:
        return

    is_consecutive = True   # is_consecutive: 단면의 모든 세로 방향에 대해서 동일한 특성의 셀들이 k개 이상 연속적으로 있는지 여부
    for j in range(w):  # 단면의 모든 세로 방향에 대해서
        consecutive_cnt = 1 # consecutive_cnt: 하나의 세로 방향에 대해서 동일한 특성의 셀들의 개수
        for i in range(d - 1):
            if film[i + 1][j] == film[i][j]:    # 동일한 특성의 셀이 있는 경우
                consecutive_cnt += 1
            else:   # 동일한 특성의 셀이 있는 경우
                consecutive_cnt = 1
            
            # 가지치기1
            # 하나의 세로 방향에 대해서 동일한 특성의 셀들이 k개 이상 연속적으로 있는 경우, 다음 세로 방향을 탐색 
            if consecutive_cnt >= k:
                break
        
        # 가지치기2
        # 하나의 세로 방향에 대해서 동일한 특성의 셀들이 k개 미만인 경우, 성능 검사를 통과하지 못함
        if consecutive_cnt < k:
            is_consecutive = False
            break
    
    if is_consecutive:  # 단면의 모든 세로 방향에 대해서 동일한 특성의 셀들이 k개 이상 연속적으로 있는 경우
        min_cnt = min(min_cnt, cnt) # 약품 투입 횟수의 최솟값 갱신
        return

    for i in range(index + 1, d):
            origin = film[i]
            # 특정 막에 약품 A를 투입하는 경우
            film[i] = [0] * w
            dfs(cnt + 1, i)
            # 특정 막에 약품 B를 투입하는 경우
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
