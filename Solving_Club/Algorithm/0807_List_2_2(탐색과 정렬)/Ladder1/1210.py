# Ladder1
"""
문제
100 x 100 크기의 2차원 배열로 주어진 사다리에 대해서, 지정된 도착점에 대응되는 출발점 x를 반환

변수

0 : 평면
1 : 사다리
2 : 도착지점
"""
import sys
sys.stdin = open('input.txt')


for tc in range(1, 11):
    T = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]

    # 바닥(99행)에서 2의 위치 찾기
    x = 99
    y = 0
    for i in range(100):
        if ladder[99][i] == 2:
            y = i
            break

    # 위로 올라가기: 좌 > 우 우선순위, 가로는 끝까지 이동 후 위로 한 칸
    while x > 0:
        # 왼쪽으로 갈 수 있으면 끝까지
        if y > 0 and ladder[x][y - 1] == 1:
            while y > 0 and ladder[x][y - 1] == 1:
                y -= 1
            x -= 1  # 가로 이동이 끝나면 위로 한 칸
        # 오른쪽으로 갈 수 있으면 끝까지
        elif y < 99 and ladder[x][y + 1] == 1:
            while y < 99 and ladder[x][y + 1] == 1:
                y += 1
            x -= 1  # 가로 이동이 끝나면 위로 한 칸
        else:
            # 양옆이 0이면 그냥 위로
            x -= 1

    print(f'#{tc} {y}')




