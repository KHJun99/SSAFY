# 백준_11660_구간_합_구하기_5 (S1)
""" 
## [문제 정리]

- N x N개의 수가 N x N 크기의 표에 채워져 있다. (x1, y1)부터
- (x2, y2)까지 합을 구하는 프로그램 작성

- 예시
    - (2, 2)부터 (3, 4)까지
        - 3 + 4 + 5 + 4 + 5 + 6 = 27
    - (4, 4)부터 (4, 4)까지
        - 7
    - 왼쪽 위 대각선 좌표, 오른쪽 아래 대각선 좌표
"""
def Prefix_Sum():
    global dp
    
    for r in range(N):
        for c in range(N):
            if c == 0:
                dp[r][c] = array[r][c]
            
            dp[r][c] = dp[r][c - 1] + array[r][c]
            
    


N , M = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(N)]
coordinates = [list(map(int, input().split())) for _ in range(M)]

dp = [([0] * N) for _ in range(N)]

Prefix_Sum()

for row in dp:
    print(row)




