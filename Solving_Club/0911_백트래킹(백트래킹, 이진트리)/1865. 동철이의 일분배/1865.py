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
input = sys.stdin.readline

def solve():
    T = int(input())
    for tc in range(1, T + 1):
        N = int(input())
        # 확률 입력 (정수 퍼센트) → 0~1로 정규화
        P = [list(map(float, input().split())) for _ in range(N)]
        for i in range(N):
            for j in range(N):
                P[i][j] *= 0.01

        # dp[mask] = mask(배정된 일들) 상태에서의 최대 성공확률(0~1)
        size = 1 << N
        dp = [-1.0] * size
        dp[0] = 1.0

        for mask in range(size):
            cur = dp[mask]
            if cur < 0:
                continue
            r = bin(mask).count('1')  # 지금 배정할 직원 인덱스
            if r == N:
                continue
            row = P[r]
            for c in range(N):
                if mask & (1 << c):    # 이미 배정된 일은 건너뜀
                    continue
                p = row[c]
                if p == 0.0:           # 0%는 가지치기
                    continue
                nxt = mask | (1 << c)
                val = cur * p
                if val > dp[nxt]:
                    dp[nxt] = val

        ans = dp[size - 1] * 100.0  # 퍼센트로 환산
        print(f"#{tc} {ans:.6f}")

if __name__ == "__main__":
    solve()
