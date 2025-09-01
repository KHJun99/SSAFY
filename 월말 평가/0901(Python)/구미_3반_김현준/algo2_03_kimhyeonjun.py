# 문제 2 : 싸피 주사위 놀이 (배점 35점)

T = int(input())
for tc in range(1, T + 1):
    N, K, E = map(int, input().split())

    dir = []
    for _ in range(E):
        start, end = map(int, input().split())
        dir.append((start, end))

    dir.sort()
    min_start = min(dir)[0]
    min_end = min(dir)[1]
    max_start = max(dir)[0]
    max_end = max(dir)[1]

    position = 0
    i = 0
    while i != K:
        if position >= N:
            position = N
            break
        position += 6
        if position >= min_start and i == 0:
            position = min_end
        if position == max_end or position == max_start:
            position -= 1

        i += 1

    print(f'#{tc} {position}')


