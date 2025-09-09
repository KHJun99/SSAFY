# 원 안의 점 (D3)
"""
문제
- 원점을 중심으로 반지름이 N인 원 안에 포함되는 격자점 (x, y 좌표가 모두 정수인 점)의 개수를 구해라.
- 즉,  x^2 + y^2 <= N^2 인 격자점의 개수를 구하여라 .
"""
import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    visited = [[None] * (N + 1) for _ in range(N + 1)]
    point = 0
    for r in range(-N, N + 1):
        for c in range(-N, N + 1):
            visited[r][c] = True
            if (r*r + c*c) <= N*N and visited:
                point += 1

    print(f'#{tc} {point}')
