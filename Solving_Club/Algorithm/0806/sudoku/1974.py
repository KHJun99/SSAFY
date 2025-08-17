# 스도쿠 검증
"""
문제
조건을 만족하는 경우 1 출력, 그렇지 않을 경우 0 출력

조건
1. 퍼즐은 모두 숫자로 채워진 상태
2. 입력으로 주어지는 퍼즐의 모든 숫자는 1 이상 9이하 정수
"""
import sys
sys.stdin = open('input.txt')

T = int(input())
N = 9

for tc in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    num = set()
    result = 1
    # 행 방향 체크
    for row in range(N):
        for col in range(N):
            num.add(sudoku[row][col])
        if len(num) != 9:
            result = 0
            break
        num.clear()

    # 열 방향 체크
    for col in range(N):
        for row in range(N):
            num.add(sudoku[row][col])
        if len(num) != 9:
            result = 0
            break
        num.clear()
    # 3*3 체크
    for row in range(0, N, 3):
        for col in range(0, N, 3):
            for i in range(3):
                for j in range(3):
                    num.add(sudoku[row + i][col + j])
            if len(num) != 9:
                result = 0
                break
        num.clear()

    print(f'#{tc} {result}')



