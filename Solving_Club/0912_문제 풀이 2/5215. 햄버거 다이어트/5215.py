# 햄버거 다이어트 (D3)
"""
## [문제 요약]

- 상황: 민기는 햄버거를 좋아하지만 다이어트 때문에 정해진 칼로리 제한을 넘지 않는 범위에서 먹으려 한다.
- 조건:
    1. 햄버거 재료는 가게에서 미리 준비해 둔 완제품 단위로만 사용 가능 (잘라 쓰기 불가).
    2. 각 재료는 한 번만 선택할 수 있음 (중복 불가).
    3. 여러 재료를 조합할 수 있으며, 총 칼로리 ≤ 제한 칼로리 여야 함.
    4. 맛 점수는 선택한 재료들의 점수 합으로 결정.

## [목표]
- 제한 칼로리 이하에서 맛 점수 합이 최대가 되는 재료 조합을 찾기.
"""
# import sys
# sys.stdin = open('sample_input.txt', 'r')


# 종료 조건 : cnt == N 일 때
# 가지의 수 : 2개 (고른다, 안고른다.)
def recur(cnt, score, cal):
    global max_cal, max_score

    if cal > L:
        return

    if cnt == N:
        max_score = max(max_score, score)
        return

    # 고른 경우
    recur(cnt + 1, score + hamburger[cnt][0] ,cal + hamburger[cnt][1])
    # 안 고른 경우
    recur(cnt + 1, score, cal)


T = int(input())
for tc in range(1, T + 1):
    # N : 재료의 수, L : 제한 칼로리
    N, L = map(int, input().split())

    # 점수, 칼로리 순서로 입력이 들어옴
    hamburger = [list(map(int, input().split())) for _ in range(N)]

    max_cal = 0
    max_score = 0
    recur(0, 0, 0)

    print(f'#{tc} {max_score}')