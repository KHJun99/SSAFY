# 백준_16987_계란으로_계란치기 (G5)
"""
## [문제 정리]
- 각 계란에는 내구도와 무게가 정해져 있다.
- 계란으로 계란을 치게 되면 각 계란의 내구도는 상대 계란의 무게만큼 깍이게 된다.
- 내구도가 0이 되는 순간 계란은 깨지게 된다.
ex)
- 계란1 : 내구도 = 7, 무게 = 5
- 계란2 : 내구도 = 3, 무게 = 4
- 계란1으로 계란2를 치게 되면
    - 계란1 : 내구도 = 7 - 4 = 3
    - 계란2 : 내구도 = 3 - 5 = -2  -> 깨짐
- 유현이가 인범이에게 알려준 퍼즐
    - 일렬로 놓여있는 계란에 대해 왼쪽부터 차례로 들어서 한 번씩만 다른 계란을 쳐 최대한 많은 계란을 깨는 문제

- 계란을 치는 과정
1. 가장 왼쪽의 계란을 든다.
2. 손에 들고 있는 계란으로 깨지지않는 다른 계란 중에서 하나를 친다.
   단, 손에 든 계란이 깨졌거나 깨지지 않은 다른 계란이 없으면 치지 않고 넘어간다.
   이후 손에 든 계란을 원래 자리에 내려놓고 3번 과정 진행
3. 가장 최근에 든 계란의 한 칸 오른쪽 계란을 손에 들고 2번 과정 진행
   단, 가장 최근에 든 계란이 가장 오른쪽에 위치한 계란일 경우 계란 치는 과정 종료

"""
def check(eggs):
    count = 0
    for egg in eggs:
        # 내구도 <= 0 이면 깨진 것
        if egg[0] <= 0:
            count += 1
    return count


def dfs(idx):
    global ans

    # 기저 조건 ( 모든 계란을 한 번씩 다 들었으면 종료 )
    if idx == N:
        # 최대 개수 갱신
        ans = max(ans, check(eggs))
        return

    # 계란이 깨졌으면
    if eggs[idx][0] <= 0:
        # 다음 계란으로
        dfs(idx + 1)
        return

    # 다른 계란을 쳤는지 확인하는 변수
    hit_any = False

    # 현재 계란으로 다른 계란 치기 시도
    for i in range(N):
        if i == idx or eggs[i][0] <= 0:
            continue

        hit_any = True

        # 내구도 계산
        eggs[idx][0] -= eggs[i][1]
        eggs[i][0] -= eggs[idx][1]

        # 다음 계란으로
        dfs(idx + 1)

        # 백트래킹
        eggs[i][0] += eggs[idx][1]
        eggs[idx][0] += eggs[i][1]

    # 칠 수 있는 계란이 없다면
    if not hit_any:
        # 다음 계란으로
        dfs(idx + 1)


N = int(input())
eggs = [list(map(int, input().split())) for _ in range(N)]
ans = 0

dfs(0)
print(ans)