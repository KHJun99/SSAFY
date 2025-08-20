# [파이썬 S/W 문제해결 기본] 6일차 - 피자 굽기
from collections import deque
import sys
sys.stdin = open('5099_input.txt')

T = int(input())
for tc in range(1, T + 1):
    # N : 화덕의 크기, M : 피자 개수
    N, M = map(int, input().split())
    pizza_cheese = list(map(int, input().split()))

    # 대기 큐: (피자번호, 치즈양)
    cheese = deque((i + 1, c) for i, c in enumerate(pizza_cheese))

    oven = deque()

    # 초기 오븐 채우기 (최대 N장)
    while len(oven) < N and cheese:
        oven.append(cheese.popleft())

    # 오븐에 1장 남을 때까지 반복
    while len(oven) > 1:
        num, c = oven.popleft()   # 맨 앞 피자 꺼내기
        c //= 2                   # 치즈 절반

        if c > 0:
            # 치즈 남았으면 다시 투입
            oven.append((num, c))
        else:
            # 치즈 다 녹았으면 버리고, 대기 피자 있으면 새로 투입
            if cheese:
                oven.append(cheese.popleft())
            # 대기 피자 없으면 그냥 오븐 장수만 줄어듦 (자연스럽게 len(oven) 감소)

    # 마지막 남은 피자 번호 출력
    print(f'#{tc} {oven[0][0]}')
