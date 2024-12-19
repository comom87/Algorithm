# 참고: https://itcrowd2016.tistory.com/84

k = int(input())
farm = [list(map(int, input().split())) for _ in range(6)]
max_width_index, max_height_index = 0, 0
max_width, max_height = 0, 0
for i in range(6):
    if farm[i][0] == 1 or farm[i][0] == 2:
        if farm[i][1] > max_width:
            max_width_index = i
            max_width = farm[i][1]
    elif farm[i][0] == 3 or farm[i][0] == 4:
        if farm[i][1] > max_height:
            max_height_index = i
            max_height = farm[i][1]

# print((max_width * max_height - abs(farm[(max_height_index - 1) % 6][1] - farm[(max_height_index + 1) % 6][1]) * abs(farm[(max_width_index - 1) % 6][1] - farm[(max_width_index + 1) % 6][1])) * k)

print((max_width * max_height - farm[(max_width_index + 3) % 6][1] * farm[(max_height_index + 3) % 6][1]) * k)