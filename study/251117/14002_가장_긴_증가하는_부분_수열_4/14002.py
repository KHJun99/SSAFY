# 백준_14002_가장_긴_증가하는_부분_수열_4 (G4)
"""
## [문제 정리]
- 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하시오.
- ex)
    - 수열 A = {10, 20, 10, 30, 20, 50}인 경우
    - 가장 긴 증가하는 부분 수열 : {10, 20, 30, 50}
    - 길이 : 4
"""
# 그냥 반복문이 아니였네..
# N = int(input())
#
# A = list(map(int, input().split()))
# tmp = []
#
# for i in range(N):
#     if i == 0:
#         tmp.append(A[0])
#
#     if tmp[-1] < A[i]:
#         tmp.append(A[i])
#
# print(len(tmp))
# print(*tmp)
N = int(input())
A = list(map(int, input().split()))

dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# 최대 길이 찾기
max_length = max(dp)
print(max_length)

# 역추적으로 실제 수열 찾기
result = []
length = max_length

for i in range(N - 1, -1, -1):
    if dp[i] == length:
        result.append(A[i])
        length -= 1

result.reverse()
print(*result)