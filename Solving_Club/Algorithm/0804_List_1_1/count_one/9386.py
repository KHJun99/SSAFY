import sys
sys.stdin = open('input1.txt')

T = int(input())

for case in range(1, T + 1):
    N = int(input())
    array = list(map(int, input().strip()))  # 공백 없이 붙어있으니 split() 대신 그대로 변환

    max_count = 0   # 연속된 1의 최대 길이
    current_count = 0  # 현재 연속된 1의 길이

    for num in array:
        if num == 1:
            current_count += 1
            if current_count > max_count:
                max_count = current_count
        else:
            current_count = 0  # 0을 만나면 연속 끊김

    print(f'#{case} {max_count}')
