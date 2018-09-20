def print_table(table):
    print("  a b c d e f g h")
    for row in range(1, 9):
        print(row, " ".join(table[row - 1]))
