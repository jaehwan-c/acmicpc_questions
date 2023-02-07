n = int(input())
lst = list()
sum_x = 0
sum_y = 0
max_x = 0
max_y = 0
x_index = 0
y_index = 0

for i in range(6):
    list_to_append = list(map(int, input().split()))
    lst.append(list_to_append)

for i in range(6):
    if lst[i][0] == 1 or lst[i][0] == 2:
        sum_x += lst[i][1]
        if max_x < lst[i][1]:
            max_x = lst[i][1]
            x_index = i
    else:
        sum_y += lst[i][1]
        if max_y < lst[i][1]:
            max_y = lst[i][1]
            y_index = i

small_index = [(x_index+3) % 6, (y_index+3) % 6] # 패턴 발견
small_area = lst[int(small_index[0])][1] * lst[int(small_index[1])][1]
print((max_x * max_y - small_area) * n)