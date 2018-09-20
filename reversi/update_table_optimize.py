def update_table_optimize(table, choice, turn_input):

    if turn_input == "B":
        turn = ["B", "W"]
    elif turn_input == "W":
        turn = ["W", "B"]
    [row, column] = [choice[0], choice[1]]
    table[row][column] = turn_input

    vectors = [[-1, 0], [1, 0], [0, -1], [0, 1],[-1, -1], [-1, 1], [1, -1], [1, 1]]
    for vector in vectors:
        i = vector[0]
        j = vector[1]
        list_i = []
        list_j = []
        while True:

            if row + i < 0 or column + j < 0 or\
               row + i > 7 or column + j > 7:
                break
            if table[row + i][column + j] == '.':
                break
            
            if table[row + i][column + j] == turn[1]:
                list_i.append(i)
                list_j.append(j)
                i += vector[0]
                j += vector[1]
                if row + i <= 7 and column + j <= 7 and\
                   row + i >= 0 and column + j >= 0:
                    if table[row + i][column + j] == turn[0]:
                        for count_i, count_j in zip(list_i, list_j):
                            if table[row + count_i][column + count_j] == turn[1]:
                                table[row + count_i][column + count_j] = turn[0]
                        break
                else:
                    break
            else:
                break
    return table
# test_table = [['W', 'B', '.', '.', 'B', '.', '.', 'B'],
#               ['.', '.', 'W', '.', 'W', '.', 'W', '.'],
#               ['B', '.', '.', 'W', 'W', 'W', '.', '.'],
#               ['B', 'W', 'W', 'W', '.', 'W', 'W', 'B'],
#               ['.', '.', '.', 'W', 'W', 'W', '.', '.'],
#               ['.', '.', 'W', '.', 'W', '.', 'W', '.'],
#               ['.', 'W', '.', '.', 'W', '.', '.', 'B'],
#               ['B', '.', '.', '.', 'B', '.', '.', '.']]
# a = update_table_optimize(test_table, [3, 4], 'B')
# for i in a:
#     print(i)
# b = ["B", "W"]
# test_choice = [5, 5]
# for i in range(8):
#     for j in range(8):
#         test_table[randint(0,7)][randint(0,7)] = b[randint(0, 1)]
#         a = update_table_optimize(test_table, [i, j], "B")
#         for k in a:
#             print(k)
