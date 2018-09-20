def valid_choice_optimize(table, player):
    # table : list[]
    list_positon = []  # list of position
    valid_moves = []  # list of valid moves
    # right, left, up, down, up_r, up_l, down_r, down_l
    list_cursor = [[1, 0], [-1, 0], [0, -1], [0, 1], [1, -1],
                   [-1, -1], [1, 1], [-1, 1]]
    # find position of player's chesses
    for i in range(len(table)):
        for j in range(len(table)):
            if player == table[i][j]:
                list_positon.append([i, j])
    for pos in list_positon:
        # consider each cursor in list_cursor
        for cursor in list_cursor:
            x, y = pos
            x_row, y_col = cursor
            if 0 <= x + x_row < 8 and 0 <= y + y_col < 8:
                if table[x + x_row][y + y_col] != player and\
                   table[x + x_row][y + y_col] != '.':
                    x += x_row
                    y += y_col
                    while 0 <= x + x_row < 8 and 0 <= y + y_col < 8:
                        if table[x + x_row][y + y_col] == player:
                            break
                        elif table[x + x_row][y + y_col] == '.':
                            valid_moves.append([x + x_row, y + y_col])
                            break
                        elif table[x + x_row][y + y_col] != player:
                            x += x_row
                            y += y_col
    # print(set(valid_moves))
    
    return sorted(valid_moves)
