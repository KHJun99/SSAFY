import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    result = 0

    # 가로 방향 검사
    for i in range(N):
        count = 0
        for j in range(N):
            if puzzle[i][j] == 1:
                count += 1
            else:
                if count == K:
                    result += 1
                count = 0
        # 한 행이 끝났을 때
        if count == K:
            result += 1

    # 세로 방향 검사
    for j in range(N):
        count = 0
        for i in range(N):
            if puzzle[i][j] == 1:
                count += 1
            else:
                if count == K:
                    result += 1
                count = 0
        # 한 열이 끝났을 때
        if count == K:
            result += 1

    print(f"#{tc} {result}")

