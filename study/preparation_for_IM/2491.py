# 수열

N = int(input())
arr = list(map(int, input().split()))

max_count = 0
count = 1
for i in range(N - 1):
    if arr[i] <= arr[i + 1]:
        count += 1
    elif arr[i] >= arr[i + 1]:
        count += 1
    else:
        if count > max_count:
            max_count = count
        count = 0

print(max_count)