# 동철이의 일 분배 (D4)
"""
문제
- N 명의 직원에게  N 개의 업무를 공평하게 하나씩 배분하려고 한다.
- 직원 번호 : 1 ~ N, 업무 번호 : 1 ~ N --> i번 직원이 j번 일을 하면 성공할 확률 = Pi,j
- 주어진 일이 모두 성공할 확률의 최댓값을 구하시오.

입력
- 첫 번째 줄 : T (테스트 케이스 수)
- 테스트 케이스의 첫 번째 줄 : N (정수)
- 다음 N개의 줄의 i 번째 줄에는 N개의 정수 Pi,1,...,i,N

"""
import sys
sys.stdin = open('input.txt', 'r')
'''
N명의 직원
N개의 일도 있음

일의 효율  P (N x N)
Pij => i 번째 직원이 j 번째 일을 하는 경우의 효율

모든 직원들이 일을 맡았을 때 최대 효율을 내는 경우를 구해야 함
i 의 사람이 j 의 일을 한다.
j는 중복되서 할 수 없고 무조건 한 사람당 하나의 일을 해야 함
순열 코드를 중심으로 문제를 해결 (중복 x)
'''


def permutation(person, work):     # person : person 번째 직원, 이전 까지의 일의 효율 정보
    global max_effi

    # 가지치기 (pruning)
    # 현재 효율이 지금까지 나온 최대 효율보다 같거나 작으면
    # 더 이상 계산해도 최대 효율보다 낮게 나옴
    # => 실수 * 실수 는 계속 값이 작아지게 되므로
    if max_effi >= work:
        return

    # 종료 조건
    if person == N:
        if max_effi < work:
            max_effi = work
        return

    for j in range(N):        # 몇 번째 일을 선택
        if not worked[j]:
            worked[j] = True
            permutation(person + 1, work * P[person][j] * 0.01)     # person + 1 : 다음 선택
            worked[j] = False


T = int(input())
for tc in range(1, T + 1):
    N = int(input())        # 직원, 일의 갯수
    P = [list(map(int, input().split())) for _ in range(N)]     # 일의 효율

    # 중복 선택을 배제할 수 있도록 방문 처리 배열 생성
    worked = [False] * N
    max_effi = 0
    permutation(0, 1)       # 1로 시작해야 일의 효율을 곱했을 때 정확한 값이 나옴

    print(f'#{tc}  {max_effi * 100 :.6f}')