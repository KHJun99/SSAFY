import sys
sys.stdin = open('sample_input (5).txt')

T = int(input())

for tc in range(1, T + 1):
    A, B = input().split()
    count = 0
    i = 0

    while i < len(A):
        if A[i : i + len(B)] == B:      # B가 발견되면
            count += 1
            i += len(B)                 # B 길이만큼 건너뛰기
        else:                           # 아니면 한 글자만 진행
            count += 1
            i += 1
    print(f'#{tc} {count}')
