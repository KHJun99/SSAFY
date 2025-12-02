# SWEA_극한의_청소_작업 (D4)
"""
## [문제 정리]
- 지하 999,999,999,999층에서 지상 999,999,999,999층에 이르는 거대한 건물 존재
- 지상
    - 1층에서부터 시작하여 999,999,999,999층까지 한 층씩 높아짐
    - 단, 숫자 4가 들어가는 모든 층은 건너 뛰어서 건설
    - 즉, 4, 14, 24, 34, 40, 41, ... , 48, 49, 53, ... 층은 생략
- 지하도 지상과 같은 방식으로 지하 1층부터 시작하여 숫자 4가 들어가는 모든 층을 건너뛰어
  지하 999,999,999,999 층까지 건설
- 입력의 편의를 위해 B (지하)를 -1로 표현
- 청소를 위해 A층에서 B층으로 올려가려고 한다.
- 올라가야하는 층 수를 구하시오.
"""
import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    A, B = map(int, input().split())

    floor = B - A - 1
    result = 0

    if -4 < A < 4 and -4 < B < 4:
        print(f'#{tc} {floor}')
        continue

    elif floor < 10:
        print(f'#{tc} {floor - 1}')
        continue

    floor_str = str(floor)
    length = len(floor_str)

    for i in range(length):
        digit = int(floor_str[length - 1 - i])
        if digit < 4:
            result += digit * (9 ** i)
        
        result += digit - 1 * (9 ** i)

    print(f'#{tc} {result}')