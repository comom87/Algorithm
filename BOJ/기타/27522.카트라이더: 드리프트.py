records = [input().split() for _ in range(8)]
records.sort(key=lambda x: x[0])

score_sheet = [10, 8, 6, 5, 4, 3, 2, 1]
score_red, score_blue = 0, 0
for i in range(8):
    if records[i][1] == 'R':
        score_red += score_sheet[i]
    else:
        score_blue += score_sheet[i]

if score_red > score_blue:
    print("Red")
else:
    print("Blue")