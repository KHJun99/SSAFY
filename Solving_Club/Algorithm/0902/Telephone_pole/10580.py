# 전봇대 (D3)
"""
문제
- 두 개의 높이가 매우 높은 전봇대가 존재한다.
- 두 전봇대는 N개의 팽팽한 전선으로 연결되어 있다.
- 두 전선의 끝점이 같은 경우는 없으나, 교차하는 경우는 존재한다.
- 세 개 이상의 전선이 하나의 점에서 만나지 않는다.
- 총 몇 개의 교차점이 존재하는지 구하시오.

"""

import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    pipe = []
    for _ in range(N):
        ai, bi = map(int, input().split())
        pipe.append((ai, bi))

    cross = 0
    for i in range(N):
        for j in range(i + 1, N):
            if pipe[i][0] < pipe[j][0] and pipe[i][1] > pipe[j][1]:
                cross += 1
            if pipe[i][0] > pipe[j][0] and pipe[i][1] < pipe[j][1]:
                cross += 1
    print(f'#{tc} {cross}')


# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     space = [0] * 100001
#     for _ in range(N):
#         ai, bi = map(int, input().split())
#         if ai > bi:
#             ai, bi = bi, ai
#         if ai != bi:
#             for i in range(ai,  bi + 1):
#                 space[i] += 1
#         else:
#             space[ai] += 1
#
#     result = space.count(2)
#     print(f'#{tc} {result}')