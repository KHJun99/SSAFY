# 백준_2304_창고_다각형 (S1)
"""
## [문제 정리]
- N개의 막대 기둥이 일렬로 세워져 있다.
- 기둥들의 폭은 모두 1m이며 높이는 다를 수 있다.
- 이 기둥들을 이용하여 양철로 된 창고를 제작하려고 한다.
- 창고에는 모든 기둥이 들어간다.
- 지붕을 만드는 규칙
    - 1. 지붕은 수평 부분과 수직 부분으로 구성되며, 모두 연결되어야 한다.
    - 2. 지붕의 수평 부분은 반드시 어떤 기둥의 윗면과 닿아야 한다.
    - 3. 지붕의 수직 부분은 반드시 어떤 기둥의 옆면과 닿아야 한다.
    - 4. 지붕의 가장자리는 땅에 닿아야 한다.
    - 5. 비가 올 때 물이 고이지 않도록 지붕의 어떤 부분도 오목하게 들어간 부분이 없어야 한다.

- 창고 다각형의 면적이 가장 작은 창고를 만들기 원한다.
- 기둥들의 위치와 높이가 주어질 때, 가장 작은 창고 다각형의 면적을 구하는 프로그램 작성
"""
N = int(input())
storage = [list(map(int, input().split())) for _ in range(N)]

storage.sort()

max_height = 0
max_height_idx = 0

for i in range(N):
    if max_height < storage[i][1]:
        max_height = storage[i][1]
        max_height_idx = i

extent = max_height  # 최대 높이 기둥의 넓이 (폭 1 * 높이)

# 왼쪽에서 최대 높이 직전까지
start_height = storage[0][1]
for i in range(1, max_height_idx + 1):
    extent += (storage[i][0] - storage[i - 1][0]) * start_height
    if storage[i][1] > start_height:
        start_height = storage[i][1]

# 오른쪽에서 최대 높이 직후부터
start_height = storage[N - 1][1]
for i in range(N - 1, max_height_idx, -1):
    extent += (storage[i][0] - storage[i - 1][0]) * start_height
    if storage[i - 1][1] > start_height:
        start_height = storage[i - 1][1]

print(extent)