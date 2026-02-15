# 백준_21608_상어_초등학교 (G5)
"""
## [문제 정리]

- 교실은 N x N 크기의 격자로 나타낼 수 있다.
    - (1, 1) : 교실의 가장 왼쪽 윗 칸
    - (N, N) : 교실의 가장 오른쪽 아랫 칸
    - (r, c)는 r행 c열을 의미

- 학교에 다니는 학생의 수는 N^2명
    - 학생은 1번부터 N^2번까지 번호가 매겨져 있다.

- 선생님은 학생의 순서를 정했다.
    - 각 학생이 좋아하는 학생 4명 모두 조사했다.
    - 규칙에 따라 정해진 순서대로 학생의 자리를 정하려 한다.

- 규칙
    - 한 칸에는 학생 한 명의 자리만 있을 수 있고,
      |r1 - r2| + |c1 - c2| = 1을 만족하는 두 칸이 (r1, c1)과 (r2, c2)를 인접하다고 한다.
    1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
    2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
    3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로,
       그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.

- 만족도 구하는 방법
    - 학생과 인접한 칸에 앉은 좋아하는 학생의 수를 구해야  한다.
    - 그 값이 0이면 학생의 만족도는 0
    - 1 이면 1
    - 2 이면 10
    - 3 이면 100
    - 4 이면 1000

- 학생의 만족도의 총 합을 구하시오.

"""
N = int(input())

classroom = [[0] * N for _ in range(N)]

# 각 학생이 좋아하는 학생들을 저장하는 딕셔너리
likes = dict()

# 학생들을 배치할 순서를 저장하는 리스트
students = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(N**2):
    student, like1, like2, like3, like4 = map(int, input().split())

    # 좋아하는 학생들을 집합(set)으로 저장
    likes[student] = {like1, like2, like3, like4}
    students.append(student)

for student in students:
    # 가능한 모든 자리의 정보 저장
    candidates = []

    # 교실의 모든 칸을 탐색
    for i in range(N):
        for j in range(N):
            # 이미 학생이 앉아있는 경우
            if classroom[i][j] != 0:
                continue
            
            # 현재 위치 (i, j)에 대한 점수 계산
            like_count = 0      # 인접한 칸 중 좋아하는 삭생의 수
            empty_count = 0     # 인접한 빈 칸의 수

            for d in range(4):
                ni = i + dx[d]      # 새로운 행 좌표
                nj = j + dy[d]      # 새로운 열 좌표

                if 0 <= ni < N and 0 <= nj < N:
                    # 인접한 칸에 좋아하는 학생이 있는 경우
                    if classroom[ni][nj] in likes[student]:
                        like_count += 1
                    # 인접한 칸이 비어있는 경우
                    elif classroom[ni][nj] == 0:
                        empty_count += 1
            
            # 내림차순을 위해 음수로 저장
            candidates.append((-like_count, -empty_count, i, j))
    
    candidates.sort()
    best_position = candidates[0]
    best_row = best_position[2]
    best_col = best_position[3]

    classroom[best_row][best_col] = student

satisfaction = 0
score_table = {0: 0, 1: 1, 2: 10, 3: 100, 4: 1000}

for i in range(N):
    for j in range(N):
        student = classroom[i][j]
        like_count = 0

        for d in range(4):
            ni = i + dx[d]
            nj = j + dy[d]

            if 0 <= ni < N and 0 <= nj < N:
                if classroom[ni][nj] in likes[student]:
                    like_count += 1
        
        satisfaction += score_table[like_count]

print(satisfaction)



