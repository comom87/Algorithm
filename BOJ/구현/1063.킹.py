import sys
input = sys.stdin.readline

king, stone, n = input().split()
direction = {
    'R': [0, 1],
    'L': [0, -1],
    'B': [1, 0],
    'T': [-1, 0],
    'RT': [-1, 1],
    'LT': [-1, -1],
    'RB': [1, 1],
    'LB': [1, -1]
}
king_x, king_y = 8 - int(king[1]), ord(king[0]) - 65
stone_x, stone_y = 8 - int(stone[1]), ord(stone[0]) - 65

for _ in range(int(n)):
    direct = input().rstrip()
    dx, dy = direction[direct]
    king_x += dx
    king_y += dy
    if king_x < 0 or king_x >= 8 or king_y < 0 or king_y >= 8:
        king_x -= dx
        king_y -= dy
        continue
    
    if king_x == stone_x and king_y == stone_y:
        stone_x += dx
        stone_y += dy
        if stone_x < 0 or stone_x >= 8 or stone_y < 0 or stone_y >= 8:
            stone_x -= dx
            stone_y -= dy
            king_x -= dx
            king_y -= dy
            continue

print(f'{chr(king_y + 65)}{8 - king_x}')
print(f'{chr(stone_y + 65)}{8 - stone_x}')