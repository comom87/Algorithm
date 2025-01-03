import sys
input = sys.stdin.readline

h, w = map(int, input().split())
blocks = list(map(int, input().split()))
total = 0
for i in range(max(blocks)):
    higher_blocks = []
    for j in range(w):
        if blocks[j] > i:
            higher_blocks.append(j)
    
    if len(higher_blocks) < 2:
        break
    
    for j in range(len(higher_blocks) - 1):
        total += higher_blocks[j + 1] - higher_blocks[j] - 1
print(total)