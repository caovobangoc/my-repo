# from print_table import *
def valid_choice(table, player):
    # table : list[]
    # x,y = table.index(player)
    list_position = []  # List of position
    valid_moves = []  # List of valid moves
    # Find positions of player's chesses
    for i in range(len(table)):
        for j in range(len(table)):
            if player == table[i][j]:
                list_position.append([i, j])
    # print(list_position)
    # move to right
    for pos in list_position:
        x, y = pos
        # print(pos)
        # Select the item which has possibility
        if y == len(table) - 1 or table[x][y + 1] == player or\
           table[x][y + 1] == '.':
            continue  # continue: move next loop, break: get out of loop
        while True:
            # print(x, y)
            if table[x][y + 1] != player:
                # print('Im here 2')
                y += 1
                if y == len(table) - 1:
                    break
                if table[x][y + 1] == player:
                    break
                if table[x][y + 1] == '.':
                    if [x, y + 1] not in valid_moves:
                        valid_moves.append([x, y + 1])
                    # print(pos,'right',valid_moves)
                    break
    # move to left
    for pos in list_position:
        x, y = pos
        if y - 1 < 0 or table[x][y - 1] == player or table[x][y - 1] == '.':
            continue
        while True:
            if table[x][y - 1] != player:
                y -= 1
                if y - 1 < 0:
                    break
                if table[x][y - 1] == player:
                    break
                if table[x][y - 1] == '.':
                    if [x, y - 1] not in valid_moves:
                        valid_moves.append([x, y - 1])
                    break
    # move down
    for pos in list_position:
        x, y = pos
        if x + 1 == len(table) or\
           table[x + 1][y] == player or\
           table[x + 1][y] == '.':
            continue
        while True:
            if table[x + 1][y] != player:
                x += 1
                if x + 1 == len(table):
                    break
                if table[x + 1][y] == player:
                    break
                if table[x + 1][y] == '.':
                    if [x + 1, y] not in valid_moves:
                        valid_moves.append([x + 1, y])
                    break
    # move up
    for pos in list_position:
        x, y = pos
        if x - 1 < 0 or table[x - 1][y] == player or table[x - 1][y] == '.':
            continue
        while True:
            # print(x, y)
            if table[x - 1][y] != player:
                x -= 1
                if x - 1 < 0:
                    break
                if table[x - 1][y] == player:
                    break
                if table[x - 1][y] == '.':
                    if [x - 1, y] not in valid_moves:
                        valid_moves.append([x - 1, y])
                    break
    # move down right
    for pos in list_position:
        x, y = pos
        # print(pos)
        if x + 1 == len(table) or\
           y == len(table) - 1 or\
           table[x + 1][y + 1] == player or\
           table[x + 1][y + 1] == '.':
            continue
        while True:
            if table[x + 1][y + 1] != player:
                x += 1
                y += 1
                # print(x, y)
                if x + 1 == len(table) or y == len(table) - 1:
                    break
                if table[x + 1][y + 1] == player:
                    break
                if table[x + 1][y + 1] == '.':
                    if [x + 1, y + 1] not in valid_moves:
                        valid_moves.append([x + 1, y + 1])
                    break
    # move down left
    for pos in list_position:
        x, y = pos
        if y - 1 < 0 or x + 1 == len(table) or\
           table[x + 1][y - 1] == player or\
           table[x + 1][y - 1] == '.':
            continue
        while True:
            if table[x + 1][y - 1] != player:
                x += 1
                y -= 1
                if y - 1 < 0 or x + 1 == len(table):
                    break
                if table[x + 1][y - 1] == player:
                    break
                if table[x + 1][y - 1] == '.':
                    if [x + 1, y - 1] not in valid_moves:
                        valid_moves.append([x + 1, y - 1])
                    break
    # move up right
    for pos in list_position:
        x, y = pos
        if x - 1 < 0 or\
           y == len(table) - 1 or\
           table[x - 1][y + 1] == player or\
           table[x - 1][y + 1] == '.':
            continue
        while True:
            if table[x - 1][y + 1] != player:
                x -= 1
                y += 1
                if x - 1 < 0 or y == len(table) - 1:
                    break
                if table[x - 1][y + 1] == player:
                    break
                if table[x - 1][y + 1] == '.':
                    if [x - 1, y + 1] not in valid_moves:
                        valid_moves.append([x - 1, y + 1])
                    break
    # move up left
    for pos in list_position:
        x, y = pos
        if y - 1 < 0 or x - 1 < 0 or\
           table[x - 1][y - 1] == player or\
           table[x - 1][y - 1] == '.':
            continue
        while True:
            if table[x - 1][y - 1] != player:
                x -= 1
                y -= 1
                if y - 1 < 0 or x - 1 < 0:
                    break
                if table[x - 1][y - 1] == player:
                    break
                if table[x - 1][y - 1] == '.':
                    if [x - 1, y - 1] not in valid_moves:
                        valid_moves.append([x - 1, y - 1])
                    break
    return sorted(valid_moves)

# print(valid_choice([['.', '.', '.', '.', '.', '.', '.', '.'],
#
#                     ['.', '.', '.', '.', '.', '.', '.', '.'],
#
#                     ['.', '.', '.', 'B', '.', '.', '.', '.'],
#
#                     ['.', '.', '.', 'B', 'B', '.', '.', '.'],
#
#                     ['.', '.', 'W', 'W', 'B', '.', '.', '.'],
#
#                     ['.', '.', '.', '.', '.', 'B', '.', '.'],
#
#                     ['.', '.', '.', '.', '.', '.', '.', '.'],
#
#                    ['.', '.', '.', '.', '.', '.', '.', '.']], 'W'))
# print_table([['.', '.', '.', '.', '.', '.', '.', '.'],
#
#                     ['.', '.', '.', '.', '.', '.', '.', '.'],
#
#                     ['.', '.', '.', 'B', '.', '.', '.', '.'],
#
#                     ['.', '.', '.', 'B', 'B', '.', '.', '.'],
#
#                     ['.', '.', 'W', 'W', 'B', '.', '.', '.'],
#
#                     ['.', '.', '.', '.', '.', 'B', '.', '.'],
#
#                     ['.', '.', '.', '.', '.', '.', '.', '.'],
#
#                     ['.', '.', '.', '.', '.', '.', '.', '.']])
