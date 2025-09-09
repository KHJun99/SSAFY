# Start 연습문제 3. 16진수 암호비트패턴 출력하기 (D2)

import sys
sys.stdin = open('input.txt', 'r')

hex_to_bin = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}

pw = {
    '001101': 0,
    '010011': 1,
    '111011': 2,
    '110001': 3,
    '100011': 4,
    '110111': 5,
    '001011': 6,
    '111101': 7,
    '011001': 8,
    '101111': 9
}
T = int(input())
for tc in range(1, T + 1):
    sample = input().strip()

    temp = []
    for i in sample:
        if i in hex_to_bin:
            temp.extend(hex_to_bin[i])

    result = []
    i = 0
    while i < len(temp):
        num = ''.join(temp[i:i + 6])
        if num in pw:
            result.append(pw[num])
            i += 6
        else:
            i += 1

    print(f'#{tc}', *result)