from random import choice

from check_move import *
from create_table import *
from encode_valid_moves import *
from print_table import *
from score import *
from update_table_optimize import *
from valid_choice_optimize import *


def reversi():
    table = create_table()
    players = ['W', 'B']
    current_player = 'W'
    count = 0
    while True:
        # Switch player
        for player in players:
            if current_player != player:
                current_player = player
                break
        # Show valide valid move
        valid_moves = valid_choice_optimize(table, current_player)
        encoded_valid_moves = encode_valid_moves(valid_moves)
        # Check if have any available move or not
        if valid_moves == []:
            print('Player %s cannot play.' % current_player)
            count += 1
            if count == 2:
                score(table)
                break
            continue
        print('Valid choices:', encoded_valid_moves)
        try:
            player_move = input('Player %s: ' % current_player)
        except EOFError:
            pass
        # User input's availability
        x = check_move(valid_moves, player_move)
        if x is False:
            print('Valid choices:', encoded_valid_moves)
            break
        _, encoded_player_move = check_move(valid_moves, player_move)
        # table = update_table_optimize(table, choice(valid_moves), current_player)
        table = update_table_optimize(table, encoded_player_move, current_player)
        # print(table)
        # Show result
        print_table(table)  # Running mode
        count = 0  # If a player can move, reset the count

if __name__ == '__main__':
    reversi()
