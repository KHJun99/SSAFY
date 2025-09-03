# import sys
# input = sys.stdin.readline

def max_score(arr):
    # arr: 원본 배열
    n = len(arr)
    # 패딩: 양끝에 1 추가
    val = [1] + arr + [1]
    # dp[l][r]: 열린 구간 (l, r) 안의 원소들을 전부 제거해 얻을 수 있는 최대 점수
    dp = [[0] * (n + 2) for _ in range(n + 2)]

    # 구간 길이를 2 이상으로 키워가며(내부 원소 수 = len-1) 채움
    for length in range(2, n + 2):           # (l, r) 간격
        for l in range(0, n + 2 - length):
            r = l + length
            best = 0
            # 마지막으로 제거되는 위치 k (l < k < r)
            for k in range(l + 1, r):
                # 이 구간에서 k가 '마지막'으로 제거될 때의 추가 점수 계산
                if l == 0 and r == n + 1:
                    # 배열 전체 구간의 마지막 제거: 그 원소 자체의 값
                    gain = val[k]
                else:
                    # 일반적인 경우: 현재 경계값들의 곱
                    gain = val[l] * val[r]

                cand = dp[l][k] + dp[k][r] + gain
                if cand > best:
                    best = cand
            dp[l][r] = best
    return dp[0][n + 1]

T = int(input().strip())
for tc in range(1, T + 1):
    N = int(input().strip())
    balloon = list(map(int, input().split()))
    ans = max_score(balloon)
    print(f"#{tc} {ans}")
