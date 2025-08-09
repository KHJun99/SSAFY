import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    arr = list(input())

    reverse_arr = arr[::-1]

    for idx in range(len(reverse_arr)):
        if reverse_arr[idx] == 'q':
            reverse_arr[idx] = 'p'
        elif reverse_arr[idx] == 'p':
            reverse_arr[idx] = 'q'
        elif reverse_arr[idx] == 'b':
            reverse_arr[idx] = 'd'
        else:
            reverse_arr[idx] = 'b'

    print(f'#{tc} ', *reverse_arr, sep='')