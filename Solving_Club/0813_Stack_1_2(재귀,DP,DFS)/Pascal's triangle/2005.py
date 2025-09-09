# 2005. 파스칼의 삼각형
import sys
sys.stdin = open('input (1).txt')
"""
규칙
1. 첫 번째 줄은 항상 숫자 1이다.
2. 두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른족 위의 숫자의 합으로 구성된다.
"""
T = int(input())
for tc in range(1, T + 1):
    N = int(input())     # N : 파스칼 삼각형 크기

    # 삼각형 크기 N의 값을 1로 초기화
    triangle = [[1] * i for i in range(1, N + 1)]

    # 규칙에 따라 값 변경
    for i in range(N - 1):
        for j in range(len(triangle[i]) - 1):
            triangle[i + 1][j + 1] = triangle[i][j] + triangle[i][j + 1]

    print(f'#{tc}')
    for i in triangle:
        print(*i)