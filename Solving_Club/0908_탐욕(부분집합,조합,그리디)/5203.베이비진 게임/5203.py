# [파이썬 S/W 문제해결 구현] 3일차 - 베이비진 게임 (D3)
"""
문제
- 0부터 9까지인 숫자 카드 4세트를 섞은 후 6개의 카드를 고른다.
- 연속인 숫자가 3개 이상이면 run
- 같은 숫자가 3개 이상이면 triple
- 교대로 한 장 씩 카드를 가져가며, 6장을 채우기 전이라도 먼저 run or triple이 되는 사람이 승자
- 만약 무승부인 경우 0 출력
"""
import sys
sys.stdin = open('5203_input.txt', 'r')


def is_babygin(cnt):
    # triple : 같은 숫자 3장
    for k in range(10):
        if cnt[k]  >= 3:
            return True

    # run : 연속된 숫자 3장
    for k in range(8):      # 0~7까지만 확인하면 됨으로
        if cnt[k] and cnt[k + 1] and cnt[k + 2]:        # 세 카드가 1이상이면 True 반환
            return True
    return False


def solve(cards):
    c1 = [0] * 10
    c2 = [0] * 10

    for i, x in enumerate(cards):
        # 짝수 인덱스 : player1 차례
        if i % 2 == 0:
            c1[x] += 1
            if is_babygin(c1):
                return 1

        # 홀수 인덱스 : player2 차례
        else:
            c2[x] += 1
            if is_babygin(c2):
                return 2
    return 0        # 승부가 나지 않을 경우


T = int(input())

for tc in range(1, T + 1):
    card = list(map(int, input().split()))
    result = solve(card)
    print(f'#{tc} {result}')