def score(table):
    count_w = 0
    count_b = 0
    for row in table:
        for item in row:
            if item == 'W':
                count_w += 1
            if item == 'B':
                count_b += 1
    print('End of the game. W: %d, B: %d' % (count_w, count_b))
    if count_w > count_b:
        print('W wins.')
    elif count_w < count_b:
        print('B wins.')
    else:
        print('Draw')


# score([['B', '.', '.', 'B', '.', 'W', 'B', 'B'],
#                    ['.', 'B', '.', 'B', '.', 'B', '.', '.'],
#                    ['.', '.', 'B', 'B', 'B', '.', '.', '.'],
#                    ['.', '.', '.', 'W', 'B', 'B', 'B', '.'],
#                    ['.', '.', 'B', 'B', 'B', '.', '.', '.'],
#                    ['.', 'B', '.', 'B', '.', 'B', '.', '.'],
#                    ['B', '.', '.', 'B', '.', '.', 'B', '.'],
#                    ['B', '.', '.', 'B', '.', '.', '.', 'B']])
