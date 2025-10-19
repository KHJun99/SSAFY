# 백준_1197_최소 스패닝 트리 (G4)
'''
## [문제]
- 그래프가 주어졌을 때, 그 그래프의 최소 스팬이 트리를 구하는 프로그램 작성
- 최소 스패닝 트리란?
    - 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리
## 접근 방법
- kruskal 알고리즘 적용
'''
# import sys
#
# input = sys.stdin.readline
# 런타임 에러 발생
# 랭크를 사용하지 않으면 파이썬 기본 재귀 한도를 넘어가게 됨 -> 런타임에러 발생
# def find_set(x):
#     if x == parents[x]:
#         return x
#
#     # 경로 압축
#     # 대표자 구하기
#     parents[x] = find_set(parents[x])
#     return parents[x]
#
#
# def union(x, y):
#     rx = find_set(x)
#     ry = find_set(y)
#
#     # 사이클 발생
#     if rx == ry:
#         return
#
#     # 일정한 규칙으로 병합 ( 더 작은 수로 )
#     if rx < ry:
#         parents[ry] = rx
#     else:
#         parents[rx] = ry


# 대표 노드 찾는 함수
def find_set(x):
    # 반복문 + 경로 압축
    while x != parents[x]:
        parents[x] = parents[parents[x]]
        x = parents[x]

    return x


# 두 집합 합치는 함수
def union(x, y):
    # 대표자 찾기
    rx, ry = find_set(x), find_set(y)

    if rx == ry:        # 사이클 발생
        return False

    # 더 큰 집합에 작은 집합을 합치기
    if size[rx] < size[ry]:
        rx, ry = ry, rx
    parents[ry] = rx
    size[rx] += size[ry]
    return True


# V : 정점의 개수, E : 간선의 개수
V, E = map(int, input().split())

# 1. 간선들을 가중치 기준으로 정렬
edges = []
for _ in range(E):
    start, end, weight = map(int, input().split())
    edges.append((start, end, weight))

# 가중치 기준 오름차순 정렬
edges.sort(key=lambda x: x[2])

# 2. 가중치가 작은 간선부터 순서대로 선택
cnt = 0         # 현재까지 선택한 간선의 수
result = 0      # 가중치의 합

# make_set
parents = [i for i in range(V + 1)]     # 자기 자신을 부모로 초기화
size = [1] * (V + 1)                    # 각 집합의 크기 (처음엔 1로 초기화)

for u, v, w in edges:
    # if find_set(u) != find_set(v):      # u, v 사이클이 아니라면
    if union(u, v):                     # 두 정점이 다른 집합이라면 MST에 포함
        cnt += 1                        # 간선 += 1
        result += w                     # 가중치 누적

        if cnt == (V - 1):              # MST 완성되는 조건
            break

print(result)