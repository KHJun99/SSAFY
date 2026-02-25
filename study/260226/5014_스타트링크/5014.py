# 백준_5014_스타트링크 (S1)
"""
## [문제 정리]

- 스트크링크 : 스타트업
    - 총 F 층으로 구성된 고층 건물에 사무실 존재
    - 스타트링크가 있는 곳의 위치 : G 층

- 강호가 지금 위치한 층 : S 층
- 엘리베이터를 타고 G층으로 이동할 예정

- 엘리베이터에는 버튼이 2개만 존재
    - U 버튼 : 위로 U층 가는 버튼
    - D 버튼 : 아래로 D층 가는 버튼
    - 만약 U층 위 또는 D층 아래에 해당하는 층이 없을 때는 이동 X
- 강호가 G층에 도착하려면, 버튼을 적어도 몇 번 눌러야 하는지 구하시오.
- 만약 엘리베이터를 이용해서 G층에 갈 수 없다면 "use the stairs" 출력
"""
from collections import deque

F, S, G, U, D = map(int, input().split())

queue = deque()
queue.append((S, 0))

floors = [False] * (F + 1)

is_goal = False
while queue:
    floor, cnt = queue.popleft()

    if floor == G:
        is_goal = True
        break
    
    floors[floor] = True

    if floor + U <= F and not floors[floor + U]:
        floors[floor + U] = True
        queue.append((floor + U, cnt + 1))

    if floor - D >= 1 and not floors[floor - D]:
        floors[floor - D] = True
        queue.append((floor - D, cnt + 1))
    

if is_goal:
    print(cnt)
else:
    print("use the stairs")
    