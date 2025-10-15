# [파이썬 S/W 문제해결 기본] 6일차 - 피자 굽기
import sys
from collections import deque

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    cheeses = list(map(int, input().split()))

    oven = deque()
    next_idx = 0  # 다음에 넣을 피자의 인덱스(0-base)

    # 처음에 오븐에 최대 N개까지 투입
    # 대기 중인 피자가 남아 있고 현재 오븐이 꽉차지 않아야 함
    while next_idx < M and len(oven) < N:
        oven.append((next_idx + 1, cheeses[next_idx]))  # (피자번호 1-base, 치즈)
        next_idx += 1

    # 한 판 남을 때까지 진행
    while len(oven) > 1:
        num, c = oven.popleft()  # 맨 앞 피자 꺼냄
        c //= 2                  # 치즈 절반
        if c > 0:
            oven.append((num, c))   # 다시 구우러 뒤로
        else:
            # 치즈 다 녹았으면 버리고, 대기 피자 있으면 즉시 투입
            if next_idx < M:
                oven.append((next_idx + 1, cheeses[next_idx]))
                next_idx += 1

    # 남은 1판의 번호 출력
    print(f'#{tc} {oven[0][0]}')
