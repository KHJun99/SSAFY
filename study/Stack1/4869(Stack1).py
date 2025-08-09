# [파이썬 S/W 문제해결 기본] 4일차 - 종이붙이기

def fill_paper(N):
    # 문제 조건 : N은 10의 배수
    if N % 10 != 0:
        return 0
    
    # dp[i] : 높이 i를 채우는 경우의 수 저장
    dp = [0] * (N + 1)
    
    dp[10] = 1      # 높이 10을 채우는 경우의 수
    dp[20] = 3      # 높이 20을 채우는 경우의 수
    
    for i in range(30, N + 1, 10):
        # 점화식 : f(x) = f(x - 10) + f(x - 20) * 2
        dp[i] = dp[i - 10] + dp[i - 20] * 2
        
    return dp[N]

T = int(input())

for i in range(1, T + 1):
    N = int(input())
    
    result = fill_paper(N)
    
    print(f'#{i} {result}')

