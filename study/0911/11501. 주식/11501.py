# 백준_11501_주식 (S2)
"""
문제
- 홍준이는 주가를 예상 가능
- 매일 아래 3가지 중 한 하나의 행동을 한다.
   1. 주식을 하나 산다.
   2. 원하는 만큼 가지고 있는 주식을 판다.
   3. 아무것도 안한다.
- 날 별로 주식의 가격을 알려주었을 때, 최대 이익을 계산
- 예시
    날 수 : 3일, 주가 : 10, 7, 6 --> 최대 이익 : 0
    날 수 : 3일, 주기 : 3, 5, 9 --> 최대 이익 : 10

입력
- 첫 줄 : T (테스트 케이스 수)
- 각 테스트 케이스 별로 자연수 N 입력 (N : 날의 수, 2<= N <= 1,000,000)
- 날 별 주가를 나타내는 N개의 자연수들이 공백으로 구분되어 순서대로 입력 (날 별 주가는 10,000 이하)

출력
- 각 테스트 케이스 별로 최대 이익을 출력
"""
import sys
sys.stdin = open('input.txt', 'r')

# 이익을 구하는 함수
def stock(lst):
    global N
    # lst의 마지막 인덱스를 최대값으로 가정
    max_price = lst[N - 1]
    price = 0

    for idx in range(N - 1, -1, -1):
        # max_price보다 리스트값이 작으면 이익 발생
        if max_price > lst[idx]:
            diff = max_price - lst[idx]
            price += diff
        # 이익이 발생할 수 없으므로 최대값 갱신
        else:
            max_price = lst[idx]

    return price


T = int(input())

for tc in range(T):
    N = int(input())
    prices = list(map(int, input().split()))

    total = stock(prices)
    print(total)