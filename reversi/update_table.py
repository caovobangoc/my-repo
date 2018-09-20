# got inputs :
# the choice of player [x, y]
# table
# player value (turn_input)
# from random import randint

def update_table(table, choice, turn_input):  # choice's format: [x, y]
    # turn_input's format: "B" or "W"
    # x : row
    # y : column

    if turn_input == "B":
        turn = ["B", "W"]
    elif turn_input == "W":
        turn = ["W", "B"]
    [row, column] = [choice[0], choice[1]]
    table[row][column] = turn[0]
    # xet hang doc cua choice:
    # xet len tren:
    i = 1  # bien dem len tren
    while True:
        if row - i >= 0:
            if table[row - i][column] == ".":
                break
            if table[row - i][column] == turn[1]:
                i += 1
                if row - i >= 0:
                    if table[row - i][column] == turn[0]:
                        for j in range(1, i):
                            if table[row - j][column] == turn[1]:
                                table[row - j][column] = turn[0]
                        break
                else:
                    break
            else:
                break
        else:
            break
    # xet xuong duoi:
    i = 1  # bien dem xuong duoi
    while True:
        if row + i < 8:
            if table[row + i][column] == ".":
                break
            if table[row + i][column] == turn[1]:
                i += 1
                if row + i < 8:
                    if table[row + i][column] == turn[0]:
                        for j in range(1, i):
                            if table[row + j][column] == turn[1]:
                                table[row + j][column] = turn[0]
                        break
                else:
                    break
            else:
                break
        else:
            break
    
    # xet hang ngang cua choice:
    # xet qua trai:
    i = 1  # bien dem qua trai
    while True:
        if column - i >= 0:
            if table[row][column - i] == ".":
                break
            if table[row][column - i] == turn[1]:
                i += 1
                if column - i >= 0:
                    if table[row][column - i] == turn[0]:
                        for j in range(1, i):
                            if table[row][column - j] == turn[1]:
                                table[row][column - j] = turn[0]
                        break
                else:
                    break
            else:
                break
        else:
            break
    # xet qua phai
    i = 1  # bien dem qua phai
    while True:
        if column + i < 8:
            if table[row][column + i] == ".":
                break
            if table[row][column + i] == turn[1]:
                i += 1
                if column + i < 8:
                    if table[row][column + i] == turn[0]:
                        for j in range(1, i):
                            if table[row][column + j] == turn[1]:
                                table[row][column + j] = turn[0]
                        break
                else:
                    break
            else:
                break
        else:
            break

    # xet hang \ cua choice:
    # xet len tren qua trai:
    i = 1  # bien dem len tren qua trai
    while True:
        if row - i >= 0 and column - i >= 0:
            if table[row - i][column - i] == ".":
                break
            if table[row - i][column - i] == turn[1]:
                i += 1
                if row - i >= 0 and column - i >= 0:
                    if table[row - i][column - i] == turn[0]:
                        for j in range(1, i):
                            if table[row - j][column - j] ==\
                                turn[1]:
                                table[row - j][column - j] =\
                                    turn[0]
                        break
                else:
                    break
            else:
                break
        else:
            break
    # xet xuong duoi qua phai:
    i = 1  # bien dem xuong duoi qua phai
    while True:
        if row + i < 8 and column + i < 8:
            if table[row + i][column + i] == ".":
                break
            if table[row + i][column + i] == turn[1]:
                i += 1
                if row + i < 8 and column + i < 8:
                    if table[row + i][column + i] == turn[0]:
                        for j in range(1, i):
                            if table[row + j][column + j] ==\
                                turn[1]:
                                table[row + j][column + j] =\
                                    turn[0]
                        break
                else:
                    break
            else:
                break
        else:
            break
    
    # xet hang / cua choice:
    # xet xuong duoi qua trai:
    i = 1  # bien dem xuong duoi qua trai
    while True:
        if row + i < 8 and column - i >= 0:
            if table[row + i][column - i] == ".":
                break
            if table[row + i][column - i] == turn[1]:
                i += 1
                if row + i < 8 and column - i >= 0:
                    if table[row + i][column - i] == turn[0]:
                        for j in range(1, i):
                            if table[row + j][column - j] ==\
                                turn[1]:
                                table[row + j][column - j] =\
                                    turn[0]
                        break
                else:
                    break
            else:
                break
        else:
            break
    # xet len tren qua phai:
    i = 1  # bien dem len tren qua phai
    while True:
        if row - i >= 0 and column + i < 8:
            if table[row - i][column + i] == ".":
                break
            if table[row - i][column + i] == turn[1]:
                i += 1
                if row - i >= 0 and column + i < 8:
                    if table[row - i][column + i] ==\
                       turn[0]:
                       for j in range(1, i):
                           if table[row - j][column + j] ==\
                              turn[1]:
                              table[row - j][column + j] =\
                              turn[0]
                       break
                else:
                    break
            else:
                break
        else:
            break
    return table


# test_table = [['W', 'B', '.', '.', '.', '.', '.', '.'],
#               ['.', '.', '.', '.', '.', '.', '.', '.'],
#               ['B', '.', '.', '.', '.', '.', '.', '.'],
#               ['W', '.', '.', '.', '.', '.', '.', '.'],
#               ['.', '.', '.', '.', '.', '.', '.', '.'],
#               ['.', '.', '.', '.', '.', '.', '.', '.'],
#               ['.', '.', '.', '.', '.', '.', '.', '.'],
#               ['.', '.', '.', '.', '.', '.', '.', '.']]


# b = ["B", "W"]
# test_choice = [5, 5]
# for i in range(8):
#     for j in range(8):
#         test_table[randint(0,7)][randint(0,7)] = b[randint(0, 1)]
#         a = update_table(test_table, [i, j], "B")
#         for k in a:
#             print(k)
