import sys
input = sys.stdin.readline

n = int(input())
waste = [list(input().rstrip()) for _ in range(n)]
recycling_waste = {'P': 0, 'C': 1, 'V': 2, 'S': 3, 'G': 4, 'F': 5}
recycling_waste_cost = list(map(int, input().split()))
general_waste_cost = int(input())

total_cost = 0
for w in waste:
    if len(set(w)) == 1:
        if list(set(w))[0] == 'O':
            total_cost += len(w) * general_waste_cost
        else:
            total_cost += min(len(w) * recycling_waste_cost[recycling_waste[list(set(w))[0]]], len(w) * general_waste_cost)
    else:
        total_cost += len(w) * general_waste_cost
print(total_cost)