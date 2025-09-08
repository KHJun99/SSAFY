import sys

sys.stdin = open('input1.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input()))
    stack = []
    count = 0
    max_count = 0

    for i in range(len(arr)):
        if arr[i] == 1:
            stack.append(arr[i])
            count += 1
            if max_count < count:
                max_count = count
        if stack and arr[i] == 0:
            stack.pop()
            count = 0
    print(f'#{tc} {max_count}')