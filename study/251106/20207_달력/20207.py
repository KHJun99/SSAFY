# 백준_20207_달력 (G5)
"""
## [문제 정리]
- 코팅지 규칙
    - 연속된 두 일자에 각각 일정이 1개 이상 있다면 이를 일정이 연속되었다고 표현
    - 연속된 모든 일정은 하나의 직사각형에 포함되어야 한다.
    - 연속된 일정을 모두 감싸는 가장 작은 직사각형의 크기만큼 코팅지를 오린다.

- 달력 규칙
    - 일정은 시작날짜와 종료날짜를 포함
    - 시작일이 가장 앞선 일정부터 차례대로 채워짐
    - 시작일이 같을 경우 일정의 기간이 긴 것이 먼저 채워짐
    - 일정은 가능한 최 상단에 배치
    - 일정 하나의 세로 길이 : 1
    - 하루의 폭 : 1

- 일정의 개수, 각 일정의 시작날짜, 종료날짜가 주어질 때 수현이가 자르는 코팅지의 면적을 구하시오.
"""
N = int(input())

day = [list(map(int, input().split())) for _ in range(N)]

last_day = max(e for s, e in day)
calendar = [0] * (last_day + 1)

for s, e in day:
    for i in range(s, e + 1):
        calendar[i] += 1

extent = 0
width = 0
height = 1

idx = 0
# 달력 순회하며 넓이 계산
for i in range(1, last_day + 1):
    if calendar[i] != 0:
        width += 1
        height = max(height, calendar[i])
    else:
        if width > 0:  # 이전에 일정이 있었다면
            extent += width * height
        width = 0
        height = 0

# 마지막 구간 처리
if width > 0:
    extent += width * height

print(extent)

