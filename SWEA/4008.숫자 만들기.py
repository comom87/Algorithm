def dfs(depth, add, subract, multiply, divide, result):
    global min_num, max_num

    if depth == n - 1:
        min_num = min(min_num, result)
        max_num = max(max_num, result)
        return

    if add > 0:
        dfs(depth + 1, add - 1, subract, multiply, divide, result + nums[depth + 1])
    if subract > 0:
        dfs(depth + 1, add, subract - 1, multiply, divide, result - nums[depth + 1])
    if multiply > 0:
        dfs(depth + 1, add, subract, multiply - 1, divide, result * nums[depth + 1])
    if divide > 0:
        if result >= 0:
            dfs(depth + 1, add, subract, multiply, divide - 1, result // nums[depth + 1])
        else:
            dfs(depth + 1, add, subract, multiply, divide - 1, -(-result // nums[depth + 1]))

t = int(input())
for test_case in range(t):
    n = int(input())
    operator = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    min_num, max_num = 1e9, -1e9
    dfs(0, operator[0], operator[1], operator[2], operator[3], nums[0])
    
    print(f'#{test_case + 1} {max_num - min_num}')