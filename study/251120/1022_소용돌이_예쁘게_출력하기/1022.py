# 백준_1022_소용돌이_예쁘게_출력하기 (G3)
"""
## [문제 정리]

- 크기가 무한인 정사각형 모눈종이 존재
    - 모눈종이 전체를 양의 정수의 소용돌이 모양으로 숫자를 채울 예정
    - 일단 숫자 1을 0행 0열에 작성
    - 0행 1열에 숫자 2를 작성
    - 반시계 방향으로 소용돌이 시작
    - 채운 소용돌이를 예쁘게 출력

- 예쁘게 출력하는 과정
    - 출력은 r1행부터 r2행까지 차례대로 출력
    - 각 원소는 공백으로 구분
    - 모든 행은 같은 길이
    - 공백의 길이는 최소
    - 모든 숫자의 길이(앞에 붙는 공백 포함)는 동일
    - 만약 수의 길이가 가장 길이가 긴 수보다 작다면,
    - 왼쪽에서부터 공백을 삽입해 길이를 맞춘다.
"""
r1, c1, r2, c2 = map(int, input().split())

n = c2 - c1
m = r2 - r1

tmp = []
for r in range(r1, r2 + 1):
    for c in range(c1, c2 + 1):
        k = max(abs(r), abs(c))

        # k=0 (원점) 특별 처리
        if k == 0:
            tmp.append(1)
            continue

        # k층 시작 번호 계산 (k >= 1)
        pre_end = (2 * k - 1) ** 2 + 1

        # 오프셋 계산
        if c == k:
            offset = k - 1 - r
        elif r == -k:
            offset = 2 * k + k - c
        elif c == -k:
            offset = 4 * k + k + r
        elif r == k:
            offset = 6 * k + k + c

        now_num = pre_end + offset
        tmp.append(now_num)

# 최댓값의 자릿수 계산
max_num = max(tmp)
width = len(str(max_num))

# 출력
for i in range(0, len(tmp), n + 1):
    print(" ".join(f"{x:{width}}" for x in tmp[i: i + n + 1]))