import sys

sys.stdin = open('sample_input.txt')


def my_max(*lst):
    list_max = lst[0]
    for num in lst[1:]:
        if num > list_max:
            list_max = num
    return list_max


for tc in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))
    total_view = 0

    # 2번째 건물부터 N-3번째까지 탐색
    for i in range(2, N - 2):
        current = buildings[i]
        left2 = buildings[i - 2]
        left1 = buildings[i - 1]
        right1 = buildings[i + 1]
        right2 = buildings[i + 2]

        max_neighbor = my_max(left2, left1, right1, right2)

        if current > max_neighbor:
            total_view += (current - max_neighbor)

    print(f"#{tc} {total_view}")



