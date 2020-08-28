from textwrap import wrap

user_input = input("Enter cells: ")
table = wrap(user_input, 3)
sep_line = "-" * 9
line = "|"


def print_row(row_number):
    return " ".join([i for i in table[row_number]])


table_format = f"""
{sep_line}
{line} {print_row(0)} {line}
{line} {print_row(1)} {line}
{line} {print_row(2)} {line}
{sep_line}"""

print(table_format)
