# Start 연습문제 1. 2진수를 10진수로 출력하기 (D2)
import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
for tc in range(1, T + 1):
    N = int(input())        # N : 문자열의 입력 개수 (7의 배수)
    arr = [list(input().strip()) for _ in range(N)]

    temp = []
    for i in range(len(arr)):
        temp.extend(arr[i])

    idx = 0
    result = []
    while idx < len(temp):
        num = ''.join(temp[idx:idx+7])
        dec = int(num.zfill(7), 2)
        result.append(dec)
        idx += 7

    print(f'#{tc}', *result)
