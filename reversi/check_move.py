# got inputs:
# list valid_moves format: [[x, y], [x, y], ...](x, y are numbers)
# player_choice(exp: c4 d3 e6 ...)(2 characters string)
def check_move(valid_moves, player_choice):
    # ma hoa player_choice thanh toa do [x, y]:
    pattern_column = ["a", "b", "c", "d", "e", "f", "g", "h"]
    pattern_row = ["1", "2", "3", "4", "5", "6", "7", "8"]
    dic = {}
    for char, num in zip('abcdefgh', range(8)):
        dic[char] = num
    # xet cu phap nhap vao phu hop hay khong
    if len(player_choice) != 2:  # input co khac 2 ky tu
        print(player_choice + ": Invalid choice")
        return False
    if player_choice[:1] not in pattern_column or\
       player_choice[1:] not in pattern_row:
        print(player_choice + ": Invalid choice")
        return False  # 1st or 2nd character invalid
    else:  # ky tu input hop le
        # xet input co trong valid_moves khong
        column = player_choice[0]
        row = int(player_choice[1])
        
        # chuyen cot thanh index
        column = dic[column]
        row = row - 1  # chuyen hang thanh index
        choice = [row, column]  # switch column and row(use later)
        if choice not in valid_moves:
            print(player_choice + ": Invalid choice")
            return False
        else:
            return True, choice
