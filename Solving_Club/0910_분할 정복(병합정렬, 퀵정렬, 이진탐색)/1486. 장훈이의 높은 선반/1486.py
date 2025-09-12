# 1486. 장훈이의 높은 선반 (D4)
"""
## [문제 요약]
- **상황**: 서점 주인 장훈은 선반(B 높이)에 물건을 올려두었음.
- **조건**: 장훈이는 키가 커서 직접 사용 가능하지만, 자리를 비웠을 때는 점원들이 물건을 꺼내야 함.
- **점원들**: 각자 키 `Hi`를 가지고 있으며, 탑을 쌓아 물건을 꺼내기로 함.

## [문제 정의]
- **탑 구성 규칙**
    1. 점원 1명만 사용할 경우 → 탑의 높이 = 그 점원의 키.
    2. 점원 여러 명이 모일 경우 → 탑의 높이 = 참여한 점원들의 키 합.
    3. 탑은 최소 1명 이상의 점원으로 이루어짐.
- **목표**
    - 탑의 높이가 **B 이상**이어야 물건을 꺼낼 수 있음.
    - **탑 높이가 높을수록 위험** → 따라서 **B 이상이면서 가장 낮은 탑 높이**를 찾아야 함.

## [접근 방법]
- 모든 탑을 쌓아 보아야 한다.
    - 조건을 만족하는 탑이 여러 개 나온다.
- 단, 가능한 탑들 중 높이가 가장 낮은 탑을 구해야 한다.
    - 모든 케이스는 확인하지 않아도 된다.
"""
import sys
sys.stdin = open('input.txt', 'r')


# 재귀함수는 종료조건과 가지의 수를 생각하고 함수를 작성해야 함.
# 종료 조건 : 모든 점원을 고려 했을 때
#   - 가지치기 : 이미 높이가 B 이상이면 더 이상 쌓을 필요 없다.
# 가지의 수 :
#   - 점원을 탑에 포함 시키는 경우 or 안시키는 경우
def recur(idx, total_height):
    global min_answer
    if total_height >= B:       # 가지치기 : B 이상이면 더 이상 쌓지 않음
        min_answer = min(min_answer, total_height)
        return

    if idx == N:        # N 명을 모두 고려함
        return

    recur(idx + 1, total_height + height[idx])      # 탑에 포함 시키는 경우
    recur(idx + 1, total_height)                    # 탑에 포함 안 시키는 경우


T = int(input())

for tc in range(1, T + 1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))

    # min_answer = 21e8           # 나올 수 있는 최대 범위 (정답이 보장된 경우)
    min_answer = 10000 * N                    # 나올 수 없다면 최대 값으로
    recur(0, 0)
    print(f'#{tc} {min_answer - B}')