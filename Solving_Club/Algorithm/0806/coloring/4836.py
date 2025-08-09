import sys

sys.stdin = open('sample_input (2).txt')


def my_sum(lst):
    total = 0
    for i in range(len(lst)):
        total += lst[i]
    return total


def my_count(lst, num):
    count = 0
    for i in range(len(lst)):
        if lst[i] == num:
            count += 1
    return count


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [[[] for _ in range(10)] for _ in range(10)]
    total = []

    for repeat in range(N):
        r1, r2, r3, r4, color = map(int, input().split())

        for i in range(r1, r3 + 1):
            for j in range(r2, r4 + 1):
                matrix[i][j].append(color)

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            total.append(my_sum(matrix[row][col]))

    result = my_count(total, 3)
    print(f'#{tc} {result}')
