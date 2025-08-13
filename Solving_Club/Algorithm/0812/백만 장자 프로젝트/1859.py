# 백만 장자 프로젝트
"""
조건
1. 연속된 N일 동안의 물건의 매매가를 알고 있다.
2. 당국의 감시망에 걸리지 않기 위해 하루에 최대 1만큼 구매 가능
3. 판매는 얼마든지 할 수 있다.
"""
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())        # 날짜를 의미
    price = list(map(int, input().split()))

    buy = [0] * (N)
    sell = 0
    for i in range(N):
        if not buy or buy[-1] >= price[i]:
            buy.append(price[i])
        else:
            sell += (int(price[i]) - int(buy[-1]))
    print(sell)