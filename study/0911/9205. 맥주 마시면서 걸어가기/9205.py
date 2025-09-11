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

접근 방법
- 각 좌표별로 거리가 1000이하이면 페스티벌 도착 가능
"""
from collections import deque
import sys
input = sys.stdin.readline

def distance(x1, y1, x2, y2):
    # 맨해튼 거리
    return abs(x1 - x2) + abs(y1 - y2)

T = int(input())
for tc in range(T):
    N = int(input())        # 편의점 개수

    home_x, home_y = map(int, input().split())       # 집 좌표
    cu = [tuple(map(int, input().split())) for _ in range(N)]  # 편의점 좌표 목록
    festival_x, festival_y = map(int, input().split())         # 페스티벌 좌표

    # BFS: 현재 위치에서 1000m 이하로 갈 수 있는 편의점들을 확장
    q = deque([(home_x, home_y)])
    visited = [False] * N   # 각 편의점 방문 여부 표시
    answer = 'sad'

    while q:
        x, y = q.popleft()

        # 현재 위치에서 바로 페스티벌로 갈 수 있으면 성공
        if distance(x, y, festival_x, festival_y) <= 1000:
            answer = 'happy'
            break

        # 방문하지 않은 편의점 중 현재 위치에서 1000m 이내인 곳을 큐에 추가
        for i, (sx, sy) in enumerate(cu):
            if not visited[i] and distance(x, y, sx, sy) <= 1000:
                visited[i] = True
                q.append((sx, sy))

    print(answer)


# import sys
# sys.stdin = open('input.txt', 'r')
#
#
# def distance(x1, y1, x2, y2):
#     diff_x, diff_y = 0, 0
#     if x1 > x2:
#         diff_x = x1 - x2
#     if y1 > y2:
#         diff_y = y1 - y2
#     if x1 < x2:
#         diff_x = x2 - x1
#     if y1 < y2:
#         diff_y = y2 - y1
#
#     dist = diff_x + diff_y
#     return dist
#
#
# def comb(cnt, start):
#     n = 2
#     if cnt == n:
#         result.append(path[:])
#         return
#
#     for i in range(start, len(all_point)):
#         path.append(all_point[i])
#         comb(cnt + 1, i + 1)
#         path.pop()
#
#
# def check():
#     dist = []
#     for i in range(len(result)):
#         dist.append(distance(result[i][0][0], result[i][0][1], result[i][1][0], result[i][1][1]))
#
#     return dist
#
#
# T = int(input())
# for tc in range(T):
#     N = int(input())        # 편의점 개수
#     cu, path, result = [], [], []
#
#     home_x, home_y = map(int, input().split())              # 집 좌표
#     home = (home_x, home_y)
#
#     for _ in range(N):
#         x, y = map(int, input().split())
#         cu.append((x, y))
#
#     festival_x, festival_y = map(int, input().split())      # 페스티벌 좌표
#     festival = (festival_x, festival_y)
#
#     all_point = [home, festival]
#     for point in cu:
#         all_point.append(point)
#
#     comb(0, 0)
#     goal = distance(home_x, home_y, festival_x, festival_y)
#
#     distance_between_points = check()
#     cnt = distance_between_points.count(1000)
#
#     if cnt * 1000 >= goal:
#         print('happy')
#     else:
#         print('sad')
