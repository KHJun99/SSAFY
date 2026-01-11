# 백준_20055_컨베이어_벨트_위의_로봇 (G5)
"""
## [문제 정리]
- 길이가 N인 컨베이어 벨트
- 길이가 2N인 벨트가 컨베이어 벤트를 위 아래로 감싸고 있다.
- 벨트는 길이 1 간격으로 2N의 칸으로 나누어져 있으며,
- 각 칸에는 1부터 2N까지의 번호가 매겨져 있다.

- 벨트가 한 칸 회전하면 1번부터 2N-1번까지의 칸은 다음 번호 칸이 있는 위치로 이동
- 2N번 칸은 1번 칸의 위치로 이동

- i번 칸의 내구도는 Ai
- 1번 칸 : 올리는 위치
- N번 칸 : 내리는 위치

- 로봇은 올리는 위치에서만 올릴 수 있다.
- 언제든지 로봇이 내리는 위치에 도달하면 즉시 내린다.
- 로봇은 컨베이어 벨트 위에서 스스로 이동 가능
- 로봇을 올리는 위치에 올리거나, 로봇이 어떤 칸으로 이동하면 내구도 1 즉시 감소

- 로봇을 옮기는 과정
    1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전
    2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면,
       이동, 이동할 수 없다면 가만히 있는다.
        1. 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며,
           칸의 내구도가 1 이상 남아 있어야 한다.
    3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    4. 내구도가 0인 칸의 개수가 K개 이상 >> 과정 종료
       그렇지 않으면 1번으로 되돌아간다.
- 종료되었을 때 몇 번째 단계가 진행 중이었는지 구하시오.
- 가장 처음에 수행되는 단계는 1번째 단계
"""
from collections import deque

# 1단계 : 회전 함수
def rotation(n):
    durability.rotate(1)
    robot_lst.rotate(1)

    # 회전 후 내리는 위치에 로봇이 있으면 바로 내림
    if robot_lst[n - 1]:
        robot_lst[n - 1] = False

# 2단계 : 로봇 이동 함수
def moving_robot(n):
    global robot_lst, durability

    for i in range(n - 2, -1, -1):
        # 현재 칸에 로봇 존재 + 다음 칸 empty + 다음 칸 내구도 1 이상
        if robot_lst[i] and not robot_lst[i + 1] and durability[i + 1] >= 1:
            robot_lst[i] = False
            robot_lst[i + 1] = True
            durability[i + 1] -= 1

    # 이동 후 내리는 위치 체크
    if robot_lst[n - 1]:
        robot_lst[n - 1] = False

# 3단계 : 올리는 위치에 있는 칸의 내구도가 0이 아니면 로봇을 올린다.
def putting_robot():
    global robot_lst, durability

    if durability[0] >= 1:
        robot_lst[0] = True
        durability[0] -= 1

# 4단계 : 내구도가 0인 칸의 개수가 K개 이상이라면 종료
def termination_condition(k):
    return durability.count(0) < k

N, K = map(int, input().split())
durability = deque(map(int, input().split()))
robot_lst = deque([False] * 2 * N)

step = 0
while termination_condition(K):
    step += 1
    rotation(N)
    moving_robot(N)
    putting_robot()

print(step)