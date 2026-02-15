# 백준_14501_퇴사 (S3)
"""
## [문제 정리]
- 오늘부터 N + 1일째 되는 날 퇴사를 하기 위해서, 남은 N일 동안 최대한 많은 상담을 진행하려 한다.
- 비서는 하루에 하나씩 서로 다른 사람의 상담을 잡아놓았다.
- 각각의 상담은 상담을 완료하는데 걸리는 기간 Ti,
- 상담을 했을 때 받을 수 있는 금액 Pi로 이루어져 있다.

- 상담을 적절히 했을 때, 백준이가 얻을 수 있는 최대 수익을 구하시오.
"""
def work(index, profit):
    global max_profit
    
    # 범위를 벗어나면 종료
    if index > N:
        max_profit = max(max_profit, profit)
        return
    
    # 현재 상담을 할 수 있는 경우
    next_index = index + schedule[index][0]
    
    if next_index <= N + 1:  # ← N+1로 변경! (퇴사일까지 일할 수 있음)
        # 상담을 하는 경우
        work(next_index, profit + schedule[index][1])
    
    # 상담을 안 하는 경우 (다음 날로)
    work(index + 1, profit)


N = int(input())

schedule = [[0, 0]]
for _ in range(N):
    T, P = map(int, input().split())
    schedule.append([T, P])

max_profit = 0

work(1, 0)

print(max_profit)
