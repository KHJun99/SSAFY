# 수열

N = int(input())
arr = list(map(int, input().split()))

count_1 = 1  # 오름차순(=non-decreasing) 길이
count_2 = 1  # 내림차순(=non-increasing) 길이
max_count_1 = 1
max_count_2 = 1

for i in range(N - 1):
    # non-decreasing
    if arr[i] <= arr[i + 1]:
        count_1 += 1
    else:
        count_1 = 1
    max_count_1 = max(max_count_1, count_1)

    # non-increasing
    if arr[i] >= arr[i + 1]:
        count_2 += 1
    else:
        count_2 = 1
    max_count_2 = max(max_count_2, count_2)

print(max(max_count_1, max_count_2))
