# 백준_16236_아기상어 (G3)
from collections import deque
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]


def bfs(si, sj):
    # [1] q, v[], 필요 자료형 생성
    q = deque()
    v = [[0] * N for _ in range(N)]
    tlst = []

    # [2] q에 초기데이터(들) 삽입, v 표시
    q.append((si, sj))
    v[si][sj] = 1
    eat = 0

    while q:
        ci, cj = q.popleft()        # q에서 데이터 한 개 꺼냄
        # eat == v[ci][cj]          # eat에 적힌 거리는 모두 리스트에 넣었음 (방문했음)
        if eat == v[ci][cj]:
            return tlst, eat - 1

        # 4 방향, 범위내, 미방문, 조건(나보다 같거나 작은경우)
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and shark >= arr[ni][nj]:
                q.append((ni, nj))
                v[ni][nj] = v[ci][cj] + 1
                # 나보다 작은 물고기인 경우 tlst에 추가
                if shark > arr[ni][nj] > 0:
                    tlst.append((ni, nj))
                    eat = v[ni][nj]
    # 방문을 모두 끝낸 경우 (먹을 물고기 못찾음..)
    return tlst, eat - 1


for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:  # 아기 상어
            ci, cj = i, j
            arr[i][j] = 0

shark = 2
cnt = ans = 0
while True:
    tlst, dist = bfs(ci, cj)
    if len(tlst) == 0:          # 더 이상 먹을 물고기 없는 경우
        break
    tlst.sort(key=lambda x: (x[0], x[1]))       # 행/열 순위로 정렬
    ci, cj = tlst[0]
    arr[ci][cj] = 0          # 물고기 먹기
    cnt += 1
    ans += dist
    if shark == cnt:    # 크기만큼 물고기 먹은 경우 + 1
        shark += 1
        cnt = 0

print(ans)

# from collections import deque
#
# N = int(input())
# space = [list(map(int, input().split())) for _ in range(N)]
#
# delta = [(-1, 0), (0, -1), (0, 1), (1, 0)]
# visited = [[False] * N for _ in range(N)]
# shirk = 2
# time = 0
# q = deque()
#
# shirk_x, shirk_y = 0, 0
# for i in range(N):
#     for j in range(N):
#         if space[i][j] == 9:
#             shirk_x, shirk_y = i, j
#             visited[shirk_x][shirk_y] = True
#             q.append((shirk_x, shirk_y))
#             while q:
#                 x, y = q.popleft()
#                 for di, dj in delta:
#                     nx, ny = x + di, y + dj
#                     if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and space[nx][ny] <= shirk:
#                         if shirk == space[nx][ny]:
#                             time += 1
#                             visited[nx][ny] = True
#                             q.append((nx, ny))
#                         else:
#                             time += 1
#                             visited[nx][ny] = True
#                             q.append((nx, ny))
#                             plus = space[nx][ny] // shirk
#                             shirk += plus
#
# print(time)