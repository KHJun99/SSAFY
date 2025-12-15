# 백준_14889_스타트와_링크 (S1)
"""
## [문제 정리]
- 축구를 하기 위해 모인 사람 : 총 N 명 ( N은 짝수 )
- 각 팀 당 N/2명 씩 팀을 나누어야 한다. (스타트 팀, 링크 팀)
- 사람 번호 : 1 ~ N 번
- Sij : i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치
- 팀 능력치 : 모든 쌍의 Sij의 합
    - i번 사람과 j번 사람이 같은 팀일 때 팀에 더해지는 능력치 : Sij, Sji
- Sij 와 Sji는 다를 수 있다.

- 스타트 팀과 링크 팀의 팀 능력치의 차이의 최소값을 구하시오.
"""


def combination(arr, r):
    result = []

    def dfs(start, selected):
        if len(selected) == r:
            result.append(selected[:])
            return

        for i in range(start, len(arr)):
            selected.append(arr[i])
            dfs(i + 1, selected)
            selected.pop()

    dfs(0, [])
    return result


N = int(input())
S = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]

members = [i for i in range(1, N + 1)]
M = N // 2

# 스타트 팀 조합 구하기
start_teams = combination(members, M)

min_diff = float('inf')

# 절반만 확인 (나머지는 대칭)
for i in range(len(start_teams) // 2):
    start = start_teams[i]

    # 링크 팀 구하기
    link = list(set(members) - set(start))

    # 스타트 팀 능력치 계산
    start_point = 0
    pairs = combination(start, 2)
    for idx1, idx2 in pairs:
        start_point += S[idx1][idx2] + S[idx2][idx1]

    # 링크 팀 능력치 계산
    link_point = 0
    pairs = combination(link, 2)
    for idx1, idx2 in pairs:
        link_point += S[idx1][idx2] + S[idx2][idx1]

    # 차이 계산
    diff = abs(start_point - link_point)
    min_diff = min(min_diff, diff)

print(min_diff)