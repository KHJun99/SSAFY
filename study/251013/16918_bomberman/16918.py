#백준_16918_봄버맨 (S1)
"""
## [문제]
- 봄버맨은 크기가 RxC인 직사각형 격자판위에 살고 있다.
- 격자의 각 칸은 비어있거나 폭탄이 들어있다.
- 폭탄은 3초가 지난 후 폭발
    - 폭탄이 폭발한 이후
        - 폭탄이 있던 칸 = 빈칸
        - 인접한 네 칸(상하좌우)도 함께 파괴
        - 연쇄반응은 없다. (인접한 칸에 폭탄이 있어도 폭발없이 파괴)
- 봄버맨은 폭탄에 면역력을 가지고 있다.
    - 격자의 모든 칸을 자유롭게 이동 가능
- 봄버맨 행동
    - 일부 칸에 폭탄 설치 (모든 폭탄이 설치되는 시간은 동일)
    - 다음 1초 동안 아무런 행동도 하지 않는다.
    - 다음 1초 동안 폭탄이 설치되어 있지 않은 모든 칸에 폭탄 설치
      (즉, 모든 칸은 폭탄을 가지고 있다, 폭탄은 모두 동시에 설치했다고 가정)
    - 1초가 지난 후에 3초 전에 설치된 폭탄이 모두 폭발
    - 3, 4를 반복
- 폭탄을 설치한 초기 상태가 주어졌을 때, N초가 흐른 후 격자판 상태를 구하여라.

## [패턴 파악]
1초 : 초기상태           grid
2초 : 전부 폭탄
3초 : 초기 폭탄 터짐     grid3라고 가정
4초 : 전부 폭탄
5초 : grid3 폭탄 터짐    grid5라고 가정
6초 : 전부 폭탄
7초 : grid5 폭탄 터짐    grid3와 같은 배열

--> 4초(3, 4, 5, 6)를 주기로 값이 반복

"""
# 폭탄 폭발
def bomb(board):
    temp = [['O'] * C for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if board[x][y] == 'O':
                temp[x][y] = '.'
                for dx, dy in delta:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < R and 0 <= ny < C:
                        temp[nx][ny] = '.'
    return temp


R, C, N = map(int, input().split())
grid = [list(input()) for _ in range(R)]

delta = [(0, 1), (1, 0), (-1, 0), (0, -1)]

if N == 1:
    ans = grid

elif N % 2 == 0:
    ans = [['O'] * C for _ in range(R)]

else:
    grid3 = bomb(grid)
    grid5 = bomb(grid3)
    ans = grid3 if N % 4 == 3 else grid5

for row in ans:
    print(*row, sep='')

