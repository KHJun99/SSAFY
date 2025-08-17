# 참외밭

K = int(input())    # 1m2 참외 개수
arr = []
for _ in range(6):
    way, field = map(int, input().split())
    arr.append((way, field))

# 큰 직사각형의 가로(width), 세로(length)
width, length = 0, 0
# 작은 직사각형의 가로(small_w), 세로(small_l)
small_w, small_l = 0, 0

for i in range(6):
    # 큰 가로 찾기 (동:1, 서:2)
    if arr[i][0] in [1, 2]:
        if arr[i][1] > width:
            width = arr[i][1]
            # 양 옆 세로 길이 차 = 작은 세로
            small_l = abs(arr[(i-1) % 6][1] - arr[(i+1) % 6][1])
            # i가 0일 경우 arr[5]가 나오는 이유
            # a, b 두 수의 몫과 나머지 관계를 만족해야함
            # a = b * q(몫) + r
            # -1 = 6 * (-1) + 5

    # 큰 세로 찾기 (남:3, 북:4)
    elif arr[i][0] in [3, 4]:
        if arr[i][1] > length:
            length = arr[i][1]
            # 양 옆 가로 길이 차 = 작은 가로
            small_w = abs(arr[(i-1) % 6][1] - arr[(i+1) % 6][1])

# 큰 직사각형 - 작은 직사각형
result = (width * length - small_w * small_l) * K
print(result)
