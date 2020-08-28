from textwrap import wrap

user_input = input("Enter cells: ")
table = [wrap(x, 1) for x in wrap(user_input, 3)]
print(table)
sep_line = "-" * 9
line = "|"


def count_cmb(smb):  # counts X or O in table
    return len([i for j in table for i in j if i == smb])


def check_win(smb):
    if table[0][0] == smb and table[1][1] == smb and table[2][2] == smb:
        return True
    elif table[0][2] == smb and table[1][1] == smb and table[2][0] == smb:
        return True
    elif table[0][0] == smb and table[1][0] == smb and table[2][0] == smb:
        return True
    elif table[0][1] == smb and table[1][1] == smb and table[2][1] == smb:
        return True
    elif table[0][2] == smb and table[1][2] == smb and table[2][2] == smb:
        return True
    elif table[0][0] == smb and table[0][1] == smb and table[0][2] == smb:
        return True
    elif table[1][0] == smb and table[1][1] == smb and table[1][2] == smb:
        return True
    elif table[2][0] == smb and table[2][1] == smb and table[2][2] == smb:
        return True
    else:
        return False


def print_row(row_number):
    return " ".join([i for i in table[row_number]])


def check_empty_cells():
    return "_" in [elem for sublist in table for elem in sublist]


table_format = f"""
{sep_line}
{line} {print_row(0)} {line}
{line} {print_row(1)} {line}
{line} {print_row(2)} {line}
{sep_line}"""

print(table_format)

if check_win("X") and check_win("O"):
    print("Impossible")
elif count_cmb("X") - count_cmb("O") > 1 or count_cmb("O") - count_cmb("X") > 1:
    print("Impossible")
elif check_win("X"):
    print("X wins")
elif check_win("O"):
    print("O wins")
elif check_empty_cells() and not check_win("X") and not check_win("O"):
    print("Game not finished")
elif not check_empty_cells():
    print("Draw")

# XOO OXO OOX check
# OOX OXO XOO check
# XOO XOO XOO check
# OXO OXO OXO check
# OOX OOX OOX check
# XXX OOO OOO check
# OOO XXX OOO check
# OOO OOO XXX check
