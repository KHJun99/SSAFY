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

def count_4(n):
    count = 0
    length = 0
    n = abs(n)

    while n > 0:
        remain = n % 10
        n = n // 10
        if remain >= 4:
            count += (remain - 1) * (9 ** length)
        else:
            count += remain * (9 ** length)
        length += 1
    return count

T = int(input())

for tc in range(1, T + 1):
    A, B = map(int, input().split())

    a = count_4(A)
    b = count_4(B)

    if A < 0 < B :
        result = a + b - 1
    else:
        result = abs(b - a)

    print(f'#{tc} {result}')
