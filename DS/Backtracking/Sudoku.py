board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7],
]

# Solve Soduko
def solve(bo):
    find = empty_postion(bo)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if safe_entry(bo, i, (row, col)):
            bo[row][col] = i
            if solve(bo):
                return True
            bo[row][col] = 0
    return False


# Check number is safe of not
def safe_entry(bo, num, postion):
    # Check for Row
    for i in bo[postion[0]]:
        if i == num:
            return False
    # Check for Column
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if j == postion[1] and bo[i][j] == num:
                return False
    # Check for Grid
    x1, y1 = ((postion[0] // 3) * 3), ((postion[1] // 3) * 3)
    x2, y2 = ((postion[0] // 3) * 3 + 3), ((postion[1] // 3) * 3 + 3)
    for i in range(x1, x2):
        for j in range(y1, y2):
            if (bo[i][j]) == num:
                return False
    return True


# Return Empty postion
def empty_postion(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)
    return None


# print board
def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


print_board(board)
print("==" * 19)
solve(board)
print_board(board)
