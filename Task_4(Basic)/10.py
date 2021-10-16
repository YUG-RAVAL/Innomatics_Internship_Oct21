def print_formatted(number,n):
    for i in range(1,n + 1):
        pad = n.bit_length()
        print(f'{i:{pad}d} {i:{pad}o} {i:{pad}X} {i:{pad}b}')