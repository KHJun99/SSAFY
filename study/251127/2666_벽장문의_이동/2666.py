# 백준_2666_벽장문의_이동 (G5)
"""
## [문제 정리]
- n 개의 같은 크기의 벽장들이 일렬로 존재
    - 문은 n - 2개만 존재
    - 한 벽장 앞에 있는 문은 이웃 벽장 앞에 문이 없다면(즉, 벽장이 열려있다면)
      그 벽장 앞으로 이동 가능
"""
n = int(input())
door1, door2 = map(int, input().split())
length = int(input())
order = [int(input()) for _ in range(length)]

closets = [0] * (n + 1)

closets[door1] = 1
closets[door2] = 1

cnt = 0
for door in order:
    if closets[door] == 0:
        if closets[door - 1] == 1:
            pass
        elif closets[door + 1] == 1:
            pass

    else:
        if closets:
            pass