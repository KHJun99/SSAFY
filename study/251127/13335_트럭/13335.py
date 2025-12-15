# 백준_13335_트럭 (S1)
"""
## [문제 정리]

- 강을 가로지르는 하나의 차선으로 된 다리가 존재
- 다리를 N개의 트럭이 건너가려고 한다.
- 트럭의 순서는 바꿀 수 없으며, 트럭의 무게는 서로 같지 않을 수 있다.
- 다리 위에는 단지 W대의 트럭만 동시에 올라갈 수 있다.
- 다리의 길이 : W 단위 길이
- 각 트럭들은 하나의 단위시간에 하나의 단위길이만큼 이동 가능
- 동시에 다리 위에 올라가 있는 트럭들의 무게의 합은
  다리의 최대하중인 L보다 작거나 같아야 한다.
- 다리 위에 완전히 올라가지 못한 틀헉의 무게는
  다리 위의 트럭들의 무게의 합을 계산할 때 포함 X
- 다리의 길이, 최대하중, 트럭들의 무게가 순서대로 주어졌을 때,
  다리를 건너는 최단시간을 구하는 프로그램을 작성하시오.

## [코드 풀이]
- 초기 상태 (예제 1)
    bridge = [0, 0]
    waiting = [7, 4, 5, 6]
    current_weight = 0
    time = 0

- 1초
    time = 1
    out = bridge.popleft() -> bridge = [0]
    current_weight = 0 - 0 = 0

    # 7톤 트럭 올라갈 수 있나? 0 + 7 = 7 <= 10 (가능)
    bridge.append(7)
    waiting = [4, 5, 6]
    current_weight = 0 + 7 = 7

    # 다리 상태
    -> bridge = [0, 7]

- 2초
    time = 2
    out = bridge.popleft() -> bridge = [7]
    current_weight = 7 - 0 = 7

    # 4톤 트럭이 올라갈 수 있나? 7 + 4 = 11 > 10 (불가능)
    bridge.append(0)
    waiting = [4, 5, 6]
    current_weight = 7

    # 다리 상태
    -> bridge = [7, 0]

- 3초
    time = 3
    out = bridge.popleft() -> bridge = [0]
    current_weight = 7 - 7 = 0

    # 3톤 트럭이 올라갈 수 있나? 0 + 4 = 4 <= 10 (가능)
    bridge.append(4)
    waiting = [5, 6]
    current_weight = 0 + 4 = 4

    # 다리 상태
    -> bridge = [0, 4]
"""
from collections import deque

# n : 다리르 건너는 트럭의 수, w : 다리의 길이, l : 다리의 최대하중
n, w, L = map(int, input().split())
trucks = list(map(int, input().split()))     # 트럭의 무게

bridge = deque([0] * w)     # 다리

current_weight = 0      # 현재 다리 위의 무게
time = 0                # 경과 시간

waiting = deque(trucks)     # 대기 중인 트럭

# 모든 트럭이 다리를 건널 때까지 반복
while waiting or current_weight > 0:
    time += 1

    # 다리의 맨 앞 트럭(없으면 빈 공간) 제거
    out = bridge.popleft()
    current_weight -= out

    if waiting:
        # 무게 조건 확인
        if current_weight + waiting[0] <= L:
            # 트럭 진입
            truck = waiting.popleft()
            bridge.append(truck)
            current_weight += truck
        else:
            # 진입 불가 - 빈 공간 추가
            bridge.append(0)
    else:
        # 대기 트럭이 없으면 빈 공간 추가
        bridge.append(0)

print(time)