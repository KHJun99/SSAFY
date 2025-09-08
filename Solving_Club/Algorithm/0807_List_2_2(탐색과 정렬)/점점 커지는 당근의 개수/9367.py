import sys

sys.stdin = open('carrot_sample_in.txt')


def carrot_size(lst):
    count = 1
    max_value = 1
    for i in range(len(lst) - 1):
        if lst[i] < lst[i + 1]:
            count += 1
            if count > max_value:
                max_value = count
        if lst[i] >= lst[i + 1]:
            count = 1
            if count > max_value:
                max_value = count

    return max_value


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    carrot = list(map(int, input().split()))

    result = carrot_size(carrot)

    print(f'#{tc} {result}')