import itertools

height = [int(input()) for i in range(9)]

for _ in itertools.combinations(height, 7):
    if sum(_) == 100:
        for j in sorted(_):
            print(j)
        break