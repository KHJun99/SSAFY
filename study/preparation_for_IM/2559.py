import sys
input = sys.stdin.readline
print = sys.stdout.write

N, K = map(int, input().split())
weather = list(map(int, input().split()))

# 첫 구간 합
window_sum = sum(weather[:K])
max_sum = window_sum

# 슬라이딩 윈도우 적용
for i in range(K, N):
    window_sum += weather[i] - weather[i-K]  # 새 값 추가, 오래된 값 제거
    if window_sum > max_sum:
        max_sum = window_sum

print(str(max_sum))
