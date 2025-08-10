import sys

sys.stdin = open('input.txt')


def dump_box(temp, count):
    for _ in range(count):
        min_value = temp[0]
        max_value = temp[0]
        min_index = 0
        max_index = 0
        # 최대값, 최대값 인덱스, 최소값, 최소값 인덱스 구하기
        for num in range(1, len(temp)):
            if temp[num] > max_value:
                max_value = temp[num]
                max_index = num
            if temp[num] < min_value:
                min_value = temp[num]
                min_index = num

        if max_value - min_value <= 1:      # 평탄화 완료인 경우
            break

        temp[max_index] -= 1
        temp[min_index] += 1

    min_value = temp[0]
    max_value = temp[0]
    for i in range(1, len(temp)):
        if temp[i] > max_value:
            max_value = temp[i]
        if temp[i] < min_value:
            min_value = temp[i]

    return max_value - min_value


for i in range(1, 11):
    dump = int(input())
    box = list(map(int, input().split()))
    print(f'#{i} {dump_box(box, dump)}')