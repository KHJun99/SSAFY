# 주사위 쌓기
"""
조건
1. 주사위의 모양은 모두 크기가 같은 정육면체
2. 마주 보는 면에 적혀진 숫자의 합은 7 X
3. 아래에서부터 1번 주사위, 2번주사위, 3번 주사위 ... 순서
4. 붙어 있는 아래 주사위의 윗면 숫자 = 위 주사위의 아랫면 숫자
5. 쌓은 주사위 옆면 숫자의 합의 최대값 구하기
"""
N = int(input())

dice_1 = list(map(int, input().split()))
dice = [list(map(int, input().split())) for _ in range(N - 1)]

min_val = float('inf')
a = dice_1[0] + dice_1[5]
b = dice_1[1] + dice_1[3]
c = dice_1[2] + dice_1[4]


