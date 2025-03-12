import sys
input = sys.stdin.readline

n = int(input())
books = {}
for _ in range(n):
    title = input().rstrip()
    if title not in books:
        books[title] = 0
    books[title] += 1
books = sorted(books.items(), key=lambda x: (-x[1], x[0]))
print(books[0][0])