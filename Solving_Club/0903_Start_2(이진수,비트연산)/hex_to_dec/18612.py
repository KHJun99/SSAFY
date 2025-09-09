# Start 연습문제 2. 16진수를 10진수로 변환하기 (D2)
import sys
sys.stdin = open('input.txt','r')

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

T = int(input())
for tc in range(1, T + 1):
    test = input().strip()

    temp = []
    for idx in test:
        if idx in hex_to_bin:
            temp.extend(hex_to_bin[idx])

    i = 0
    result = []
    while i < len(temp):
        num = ''.join(temp[i:i+7])
        result.append(int(num.zfill(7), 2))
        i += 7

    print(f'#{tc}', *result)