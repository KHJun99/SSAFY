# 백만 장자 프로젝트
import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input().strip())
for tc in range(1, T + 1):
    N = int(input().strip())
    prices = list(map(int, input().split()))

    max_price = 0   # 오른쪽에서부터 본 최고가(그날 전량 매도한다고 가정)
    profit = 0      # 누적 이익(파이썬 int는 큰 수 OK)

    # 오른쪽 → 왼쪽으로 스캔
    for p in reversed(prices):
        if p <= max_price:
            # 오늘 사서 미래의 최고가(max_price)에 판다
            profit += (max_price - p)
        else:
            # 더 비싼 날 발견 → 그날이 새로운 '매도 기준가'
            max_price = p

    print(f'#{tc} {profit}')
