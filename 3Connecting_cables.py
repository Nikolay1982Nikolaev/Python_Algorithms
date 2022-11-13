
" 2 5 3 8 7 4 6 9 1 "
cables = [int(x) for x in input().split()]
size = len(cables) + 1
position = [pos for pos in range(1, size)]

lcs = []
[lcs.append([0] * size) for _ in range(size)]


for row in range(1, size):
    for col in range(1, size):
        if cables[row - 1] == position[col - 1]:
            lcs[row][col] = lcs[row-1][col-1] + 1

        else:
            lcs[row][col] = max(lcs[row -1 ][col] , lcs[row][col-1])

print(f"Maximum pairs connected: {lcs[size-1][size -1]}")



