import sys

sys.stdin = open('sample_input.txt')


def my_max(lst):
    max_val = float('-inf')
    for i in lst:
        if max_val < i:
            max_val = i
    return max_val


for tc in range(1, 11):
    N = int(input())
    building = list(map(int, input().split()))
    room = 0

    for i in range(2, N - 2):
        left_build_1 = building[i - 1]
        left_build_2 = building[i - 2]
        right_build_1 = building[i + 1]
        right_build_2 = building[i + 2]

        height = [left_build_1, left_build_2, right_build_1, right_build_2]
        max_height = my_max(height)

        diff = building[i] - max_height
        if diff > 0:
            room += diff

    print(f'#{tc} {room}')