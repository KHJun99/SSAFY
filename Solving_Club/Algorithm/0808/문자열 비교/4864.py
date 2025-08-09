import sys

sys.stdin = open('4864_input.txt')

T = int(input())

for tc in range(1, T + 1):
    str1 = input()
    str2 = input()

    if str1 in str2:
        result = 1
    else:
        result = 0
    print(f'#{tc} {result}')