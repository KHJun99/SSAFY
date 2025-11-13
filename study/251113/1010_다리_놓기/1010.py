# 백준_1010_다리_놓기 (S4)
"""
## [문제 정리]
- 재원이는 강을 건널 수 있는 다리를 짓기로 결심하였다.
- 사이트 : 다리를 짓기에 적합한 곳
- 서쪽 : N개의 사이트, 동쪽 : M개의 사이트 (N <= M)
- 한 사이트에는 최대 한 개의 다리만 연결 가능
- 서쪽의 사이트 개수(N)개 만큼 다리를 지으려고 한다.
- 다리끼리 서로 겹쳐질 수 없다고 할 때 다리를 지을 수 있는 경우의 수를 구하는 프로그램 작성

case1) N = 2, M = 2 -> 2C2
n=0:           1
n=1:         1   1
n=2:       1   2   1
           ↑   ↑
         r=0  r=1  r=2

case2) N = 1, M = 5 -> 5C1
n=0:                   1
n=1:                 1   1
n=2:               1   2   1
n=3:             1   3   3   1
n=4:           1   4   6   4   1
n=5:         1   5  10  10   5   1
             ↑   ↑
           r=0  r=1  r=2  r=3  r=4  r=5

case3) N = 13, M = 29 -> 29C13

n=0:  1
n=1:  1   1
n=2:  1   2   1
n=3:  1   3   3   1
n=4:  1   4   6   4   1
n=5:  1   5  10  10   5   1
n=6:  1   6  15  20  15   6   1
n=7:  1   7  21  35  35  21   7   1
...
n=13: 1  13  78  286  715  1287  1716  1716  1287  715  286  78  13   1
...
n=29: 1  29  ...  [중간 생략]  ...  67863915(13번째)  ...  29   1
"""
def combination(n, r):
    dp = [[0] * (r + 1) for _ in range(n + 1)]

    # 초기값 : nC0 = 1
    for i in range(n + 1):
        dp[i][0] = 1

    # 파스칼 삼각형 : dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
    for i in range(1, n + 1):
        for j in range(1, min(i, r) + 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

    return dp[n][r]


T = int(input())
result = []
for _ in range(T):
    N, M = map(int, input().split())

    result.append(combination(M, N))

for row in result:
    print(row)