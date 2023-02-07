m, n = map(int, input().split())
board_input = []
lst_to_print = []

for i in range(m):
    board_input.append(input())

for i in range(m-7):
    for j in range(n-7):
        black = 0
        white = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0:
                    if board_input[k][l] != 'W':
                        black += 1
                    if board_input[k][l] != 'B':
                        white += 1
                else:
                    if board_input[k][l] != 'B':
                        black += 1
                    if board_input[k][l] != 'W':
                        white += 1  
        lst_to_print.append(min(black, white))

print(min(lst_to_print))