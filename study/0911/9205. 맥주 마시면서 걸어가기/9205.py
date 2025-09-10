# 백준_9205_맥주 마시면서 걸어가기 (G5)
"""
문제
- 상근이네 집에서 맥주 한박스를 들고 출발한다.
- 맥주 한박스에는 맥주가 20개 들어있다.
- 50미터에 한 병씩 마시려고 한다. 즉, 50미터를 가려면 그 직전에 맥주 한병을 마셔야 한다.
- 가는 길에 편의점에서 맥주를 더 구매해야 할 수도 있다.
- 편의점에 들렸을 때, 빈 병은 버리고 새 맥주 병을 살 수 있다.
- 하지만, 박스에 들어있는 맥주는 20병을 넘을 수 없다.
- 편의점을 나선 직후에도 50미터를 가기 전에 맥주 한 병을 마셔야 한다.

입력
- 첫 째줄 : T (테스트 케이스 개수)
- 각 테스트 케이스의 첫 째줄 : n (편의점의 개수)
- 다음 n + 2개의 줄 : 상근이네 집, 편의점, 페스티벌 좌표 (x, y로 구성)
  ( -32768 <= x, y <= 32767 )
- 송도는 직사각형 모양으로 생긴 도시 --> 두 좌표 사이의 거리 : x 좌표의 차이 + y 좌표의 차이

출력
- 상근이와 친구들이 행복하게 페스티벌에 갈 수 있으면 'happy'
- 중간에 맥주가 바닥나서 더 이동할 수 없으면 'sad' 출력

"""
import sys
sys.stdin = open('input.txt', 'r')


def distance(x1, y1, x2, y2):
    diff_x, diff_y = 0, 0
    if x1 > x2:
        diff_x = x1 - x2
    if y1 > y2:
        diff_y = y1 - y2
    if x1 < x2:
        diff_x = x2 - x1
    if y1 < y2:
        diff_y = y2 - y1

    dist = diff_x + diff_y
    return dist


T = int(input())
for tc in range(T):
    N = int(input())        # 편의점 개수
    cu = []
    home_x, home_y = map(int, input().split())              # 집 좌표
    for _ in range(N):
        x, y = map(int, input().split())
        cu.append((x, y))
    festival_x, festival_y = map(int, input().split())      # 페스티벌 좌표

    print(distance(home_x, home_y, festival_x, festival_y))