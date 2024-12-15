from collections import deque

n = int(input())
cards = deque([i for i in range(1, n + 1)])
while cards:
    print(cards.popleft(), end=' ')
    if not cards:
        break
    cards.append(cards.popleft())