# 백준_16967_배열_복원하기 (S3)
"""
## [문제 정리]

- 크기가 H x W 인 배열 A 와 두 정수 X와 Y가 있을 때,
- 크기가 (H + X) x (W + Y)인 배열 B는 
- 배열 A와 배열 A를 아래로 X칸, 오른쪽으로 Y칸 이동시킨 배열을 겹쳐서 생성 가능
- 수가 겹쳐지면 수가 합쳐진다.

- 배열 B의 (i, j)에 들어있는 값은 아래 3개 중 하나
    1. 두 배열에 모두 포함되지 않으면, Bij = 0
    2. 두 배열에 모두 포함되면, Bij = Aij + A(i-X)(j-Y)
    3. 두 배열 중 하나에 포함되면, Bij = Aij or Bij = A(i-X)(j-Y)

배열 B와 정수 X, Y가 주어졌을 때, 배열 A를 구하시오.
"""
H, W, X, Y = map(int, input().split())

array_B = []
for _ in range(H + X):
    array = list(map(int, input().split()))
    array_B.append(array)

array_A = [[0] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if i < X or j < Y:
            # 겹치지 않은 부분
            array_A[i][j] = array_B[i][j]
        else:
            # 겹친 부분
            array_A[i][j] = array_B[i][j] - array_A[i - X][j - Y]

for row in array_A:
    print(*row)