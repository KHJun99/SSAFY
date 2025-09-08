# [파이썬 S/W 문제해결 구현] 3일차 - 화물 도크 (D3)
"""
문제
- 0시부터 다음날 0시 이전까지 A도크의 사용신청을 확인해 최대한 많은 화물차가 화물을 싣고 내릴 수 있도록 하면,
  최대 몇 대의 화물차가 이용할 수 있는지 알아내 출력하는 프로그램을 만드시오.
- 신청서 : 작업 시작 시간, 완료 시간이 매시 정각을 기준으로 표시
- 앞작업의 종료와 동시에 다음 작업 시작 가능

입력
- 첫 줄에 테스트 케이스의 수 T 주어진다.
- 다음 줄부터 테스트 케이스 별로 첫 줄에 신청서 N 입력
- 다음 줄부터 N개의 줄에 걸쳐 화물차의 작업 시작 시간 s, 종료 시간 e 주어진다.
- 1 <= N <= 100, 0 <= s < 24, 0 < e <= 24
"""
import sys
sys.stdin = open('5202_input.txt', 'r')


def time():
    result = [schedule[0]]
    i = 0
    j = 1
    while j != len(schedule):
        if result[i][1] <= schedule[j][0]:
            result.append(schedule[j])
            i += 1
            j += 1
        else:
            j += 1
    return result


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    schedule = []
    for _ in range(N):
        s, e = map(int, input().split())
        schedule.append((s, e))

    # 종료 시간 기준 정렬
    schedule.sort(key=lambda x:x[1])

    result = time()
    print(f'#{tc} {len(result)}')




