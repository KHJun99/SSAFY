def hex_to_bin(hex):
    if hex == 'A':
        deci = 10
    elif hex == 'B':
        deci = 11
    elif hex == 'C':
        deci = 12
    elif hex == 'D':
        deci = 13
    elif hex == 'E':
        deci = 14
    elif hex == 'F':
        deci = 15
    else:
        deci = int(hex)
    bin = ''
    d = 3
    for _ in range(4):
        bit = deci // 2 ** d
        bin += str(bit)
        deci -= 2 ** d * bit
        d -= 1
    return bin


T = int(input())
for tc in range(1, T + 1):
    bit_sequence = ''
    hex_sequence = input()
    for hex in hex_sequence:
        bit_sequence += hex_to_bin(hex)
    bit_len = len(bit_sequence)
    deci_list = []
    deci = 6
    num = 0
    for bit in bit_sequence[:(bit_len - bit_len % 7)]:
        num += int(bit) * 2 ** deci
        deci -= 1
        if deci == -1:
            deci_list.append(num)
            num = 0
            deci = 6
    deci = bit_len % 7 - 1
    num = 0
    for bit in bit_sequence[(bit_len - bit_len % 7):]:
        num += int(bit) * 2 ** deci
        deci -= 1
    deci_list.append(num)

    print(f'#{tc} ', end='')
    print(' '.join(map(str, deci_list)))
