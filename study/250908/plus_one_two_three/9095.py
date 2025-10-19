# 백준_9095_1,2,3 더하기 (S3)
"""
문제
- 정수 n이 주어졌을 때, n을 1, 2, 3의 합으로 나타내는 방법의 수를 구하는 프로그램을 작성

입력
- 첫째 줄 : 테스트 케이스의 개수 T
- T만큼 n이 주어진다.

접근방법
- 점화식 구하기
"""
def one_two_three(n):
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, n + 1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    return(dp[n])


# n은 양수이며 11보다 작기 때문
dp = [0] * 11
T = int(input())
for tc in range(T):
    n = int(input())

    cnt = one_two_three(n)
    print(cnt)