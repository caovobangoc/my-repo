def create_table():
    """###########ERROR################"""
    # table = [['.']*8]*8
    # table[3][3]= 'W'
    """Not work because same allocation"""
    table = []
    for i in range(8):
        table.append([])
    for row in table:
        for i in range(8):
            row.append('.')
    table[3][3] = 'W'
    table[3][4] = 'B'
    table[4][3] = 'B'
    table[4][4] = 'W'
    # for row in table:
    #     print(row)
    # Print header
    print('  a b c d e f g h')
    for row in range(1, 9):
        print(row, " ".join(table[row - 1]))
    return table

# def player_turn
# create_table()
