# 백준_1647_도시 분할 계획 (G4)
'''
## [문제]
- 마을
    - N개의 집과 그 집들을 연결하는 M개의 길로 이루어짐
    - 무방향 길
    - 유지비 존재
    - 임의의 두 집 사이에 경로가 항상 존재
- 마을 분활
    - 분리된 마을 안에 있는 임의의 두 집 사이에 경로가 항상 존재
    - 집이 하나 이상 존재
    - 두 마을 사이에 있는 길들은 삭제
    - 마을 안에서도 임의의 두 집사이의 최소 경로만 존재하고 나머지 삭제
- 유지비의 합을 최소로 하는 프로그램 작성
'''
# 시간초과
# input = sys.stdin.readline 후 통과

import sys
input = sys.stdin.readline
def find_set(x):
    while x != parents[x]:
        parents[x] = parents[parents[x]]
        x = parents[x]
    return x


def union(x, y):
    rx, ry = find_set(x), find_set(y)

    if rx == ry:
        return False

    if size[rx] < size[ry]:
        rx, ry = ry, rx
    parents[ry] = rx
    size[rx] += size[ry]
    return True


# N : 집의 개수 , M : 길의 개수
# 2 <= N <= 100,000
# 1 <= M <= 1,000,000
N, M = map(int, input().split())

edges = []
for _ in range(M):
    start, end, weight = map(int, input().split())
    edges.append((start, end, weight))

edges.sort(key=lambda x: x[2])

parents = [i for i in range(N + 1)]
size = [1] * (N + 1)

cnt = 0
result = 0
# MST에 포함된 간선 중 가장 큰 가중치 저장
# 두 마을을 생성하기 위해서는 하나의 간선을 끊어야 함
# 가장 비싼 간선을 끊는 게 전체 유지비 최소화
max_edge = 0

for u, v, w in edges:
    if union(u, v):
        cnt += 1
        result += w
        max_edge = w

        if cnt == (N - 1):
            break

print(result - max_edge)

