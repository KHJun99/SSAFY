import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    word = list(input())
    result = 0
    if word == word[::-1]:
        result = 1

    print(f'#{tc} {result}')