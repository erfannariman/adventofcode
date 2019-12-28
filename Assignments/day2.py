def read_data(filename):

    with open(f'../Puzzle_inputs/{filename}') as f:
        # split string on comma and cast to integers
        data = [int(code) for code in f.read().split(',')]

    return data


def restore_code():

    codes = read_data('day2.txt')

    # change values on position 1 & 2:
    codes[1] = 12
    codes[2] = 2

    for i in range(0, len(codes), 4):
        chunk = codes[i: i+4]

        try:
            pos1, pos2, pos3, pos4 = chunk[0], chunk[1], chunk[2], chunk[3]
        except IndexError:
            break

        if pos1 == '99':
            print(f'99 in code: {chunk}')
            break

        # if first code is 1, then it's addition
        elif pos1 == 1:
            codes[pos4] = codes[pos2] + codes[pos3]

        # else if first code is 2, then it's multiplication
        else:
            codes[pos4] = codes[pos2] * codes[pos3]

    return codes


if __name__ == '__main__':
    restored_codes = restore_code()
    print(restored_codes[0])
