# 백준_12886_돌_그룹 (G4)
"""
## [문제 정리]
- 돌은 세 개의 그룹으로 나누어져 있다
    - 각각의 그룹에는 돌이 A, B, C개 존재
- 강호는 모든 그룹에 있는 돌의 개수를 같게 만들려고 한다.
- 돌을 움직이는 단계
    - 크기가 같지 않은 두 그룹을 고른다.
    - 돌의 개수가 작은 쪽을 X, 큰 쪽을 Y라고 정한다.
    - 그 다음, X에 있는 돌의 개수를 X + X개,
    - Y에 있는 돌의 개수를 Y - X 개로 만든다.
- A, B, C 가 주어졌을 때, 강호가 돌을 같은 개수로 만들 수 있으면 1,
- 아니면 0을 출력하는 프로그램 작성
"""
from collections import deque


def rock_game(a, b, c):
    queue = deque([(a, b, c, 0)])
    visited = set()
    visited.add((a, b, c))

    while queue:
        n1, n2, n3, turn = queue.popleft()

        if n1 == n2 == n3:
            return 1

        if turn % 2 == 0:
            if n1 != n2:
                if n1 > n2:
                    new_state = (n1 - n2, n2 * 2, n3)
                else:
                    new_state = (n1 * 2, n2 - n1, n3)

                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((*new_state, turn + 1))
            else:
                queue.append((n1, n2, n3, turn + 1))
        else:
            if n2 != n3:
                if n2 > n3:
                    new_state = (n1, n2 - n3, n3 * 2)
                else:
                    new_state = (n1, n2 * 2, n3 - n2)

                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((*new_state, turn + 1))
            else:
                queue.append((n1, n2, n3, turn + 1))
    return 0


A, B, C = map(int, input().split())

print(rock_game(A, B, C))