#   a b c d e f g h
# 1 . . . . . . . .
# 2 . . . . . . . .
# 3 . . . . . . . .
# 4 . . . W B . . .
# 5 . . . B W . . .
# 6 . . . . . . . .
# 7 . . . . . . . .
# 8 . . . . . . . .


def encode_valid_moves(valid_moves):
    list_encode_valid_moves = []
    return_encode = []
    return_string = ' '
    # encode valid moves to string x : rows, y : column
    # pattern_column = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    dic = {}
    for num, char in zip(range(8), 'abcdefgh'):
        dic[num] = char
    for pos in valid_moves:
        x, y = pos
        # encode collum to char
        column = dic[y]
        row = str(x + 1)
        if [column, row] not in list_encode_valid_moves:
            list_encode_valid_moves.append([column, row])
    list_encode_valid_moves = sorted(list_encode_valid_moves)
    for item in list_encode_valid_moves:
        position = ''.join(item)
        return_encode.append(position)
    return_string = ' '.join(return_encode)
    # print(return_string)
    return return_string

# print(encode_valid_moves([[3, 4], [4, 3]]))
