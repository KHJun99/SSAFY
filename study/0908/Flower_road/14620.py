# 백준_14620_꽃길 (S2)
"""
문제
- 꽃을 심고나면 정확히 1년후에 핀다.
- 진아는 꽃의 씨앗을 세개 가지고 있다.
- 세 개의 꽃이 하나도 죽지 않고 1년 후에 꽃잎이 만개하길 원한다.
- 꽃밭은 NxN의 격자 모양이고 (1,1)~(N,N)의 지점 중 한 곳에 심을 수 있다.
- 씨앗이 만개하면 씨앗기준으로 상하좌우 1칸씩 증가
- 어떤 씨앗이 꽃이 핀 뒤 다른 꽃잎(혹은 꽃술)과 닿게 될 경우 두 꽃 모두 죽는다.
- 또한 화단 밖으로 꽃잎이 나가게 된다면 그 꽃은 죽어버린다.
- 화단의 대여 가격은 격자의 한 점마다 다르다.
- 꽃 하나당 5평의 땅을 대여해야 한다.
- 서로 다른 세 씨앗을 모두 꽃이 피게하면서 최소 비용을 구하여라.

입력
- 첫째 줄에 화단의 한 변의 길이 (N) 입력
- 이후 N개의 줄에 N개씩 화단의 지점담 가격이 주어진다.

구현방법
- 꽃잎의 범위를 만족하며 심을 수 있는 꽃술의 위치를 찾는다.
- 만족하는 경우의 수를 비교하면서 업데이트 한다.
"""
# 꽃이 필 수 있을 때의 합을 구하는 함수
def flower_sum_with_cells(lst):
    """
    각 꽃 중심 후보에 대해:
      - idx   : 일련번호 (1부터 시작)
      - cost  : 해당 꽃을 심을 때 드는 총 비용
      - cells : 꽃이 차지하는 5칸 좌표 집합
    을 리스트로 반환
    """
    N = len(lst)  # 격자 한 변의 길이 (N x N)
    delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    items = []  # 최종 결과를 담을 리스트 [(idx, cost, cells), ...]
    i = 1       # 후보 일련번호

    for r in range(1, N - 1):
        for c in range(1, N - 1):
            # 현재 후보가 점유할 좌표 집합을 만들기 시작 (먼저 중심칸 추가)
            cells = {(r, c)}
            # 현재 후보의 비용 시작값은 중심칸의 비용
            cost = lst[r][c]
            ok = True  # 이 후보가 유효한지(격자 밖/중복 점유 없는지) 플래그
            # 상하좌우 4칸을 추가로 점유
            for dr, dc in delta:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < N:
                    cells.add((nr, nc))      # 점유 좌표 추가
                    cost += lst[nr][nc]      # 비용 누적
                else:
                    ok = False               # 불가 판정
                    break

            # 유효한 후보만 수집
            if ok:
                items.append((i, cost, cells))
            i += 1

    return items  # 예: [(1, 12, {(2,2),(1,2),(3,2),(2,1),(2,3)}), (2, 15, {...}), ...]


def no_overlap(cells_a, cells_b):
    """
    - isdisjoint: 두 집합에 교집합이 없으면 True, 있으면 False
    - 반환: 겹치지 않으면 True(= 배치 가능), 겹치면 False(= 불가)
    """
    return cells_a.isdisjoint(cells_b)


def comb_no_overlap(m, cells_list):
    """
    1..m(= 후보 일련번호)의 범위에서 3개를 뽑아,
    '세 후보 모두' 서로 겹치지 않는 조합만 모아 반환합니다.

    - 이중·삼중 루프를 통해 오름차순 조합 (a < b < c)만 생성
    - 각 단계에서 즉시 겹침을 걸러내어(가지치기) 불필요한 탐색을 줄임
    - 반환 형식: [(a, b, c), ...]  (a,b,c는 후보 idx)
    """
    res = []
    for a in range(1, m + 1):
        for b in range(a + 1, m + 1):
            # 1차 가지치기: a와 b가 겹치면 더 진행할 필요 없음
            if not no_overlap(cells_list[a], cells_list[b]):
                continue
            for c in range(b + 1, m + 1):
                # 2차 가지치기: a-c, b-c 모두 겹치지 않아야 최종 채택
                if no_overlap(cells_list[a], cells_list[c]) and no_overlap(cells_list[b], cells_list[c]):
                    res.append((a, b, c))
    return res


N = int(input().strip())
flower = [list(map(int, input().split())) for _ in range(N)]

# 1) 모든 중심 후보에 대한 (idx, cost, cells) 전처리
items = flower_sum_with_cells(flower)

# 후보 총개수: (N-2)^2 개 (중심 가능한 칸 수)
m = len(items)

costs = [0] * (m + 1)               # 해당 후보의 비용
cells_list = [set()] * (m + 1)      # 해당 후보가 점유하는 5칸 좌표 집합

for idx, cost, cells in items:
    costs[idx] = cost
    cells_list[idx] = cells

# 유효한 3개 조합 추출
valid_triples = comb_no_overlap(m, cells_list)

# 2) 각 유효 조합(a,b,c)에 대해 비용 합산 후 최소값 탐색
ans = None
for a, b, c in valid_triples:
    total_cost = costs[a] + costs[b] + costs[c]
    if ans is None or total_cost < ans:
        ans = total_cost

print(ans)

