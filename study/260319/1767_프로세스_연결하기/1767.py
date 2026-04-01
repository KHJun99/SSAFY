# SWEA_1767_프로세스_연결하기 
"""
## [문제 정리]

- 프로세서(멕시노스) : N x N 개의 cell로 구성
    - 1개의 cell에는 코어 또는 전선이 올 수 있다.
    - 가장자리에는 전원이 흐르고 있다.

- 전선 설치 규칙
    - 직선으로만 설치 가능
    - 교차 설치 불가능

- 초기상태 : 전선 연결 전 멕시노스 정보
    - 가장자리에 위치한 코어는 이미 전원이 연결된 상태

- 최대한 많은 코어에 전원을 연결, 전선 길이의 합을 구하고자 한다.
    - 단, 여러 방법이 있을 경우, 전선의 길이의 합이 최소가 되는 값을 구하시오.

- 제약 사항
    1. 7 <= N <= 12
    2. 코어의 개수 : 1개 이상 12개 이하
    3. 최대한 많은 코어에 전원을 연결해도,
       전원이 연결되지 않는 코어가 존재할 수 있다.
"""
import sys
sys.stdin = open('sample_input.txt')

def is_connect(r, c, d):
    nr, nc = r, c
    while True:
        nr += dr[d]
        nc += dc[d]

        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            return False
        if init[nr][nc] != 0:
            return False
        if nr == 0 or nr == N - 1 or nc == 0 or nc == N - 1:
            return True 


def dfs(core_cnt, wire):
    global total_wire, init

    if core_cnt == len(cores):
        total_wire = min(total_wire, wire)
        return

    r, c = cores[core_cnt]

    for idx in range(4):
        if is_connect(r, c, idx):
            length = 0
            nr, nc = r + dr[idx], c + dc[idx]
            while nr != 0 or nr != N - 1 or nc != 0 or nc != N - 1:
                init[nr][nc] = 2
                length += 1
                nr += dr[idx]
                nc += dc[idx]
            dfs(core_cnt + 1, wire + length)
            while nr != 0 or nr != N - 1 or nc != 0 or nc != N - 1:
                init[nr][nc] = 0
                
    
    dfs(core_cnt + 1, wire)
    

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    init = [list(map(int, input().split())) for _ in range(N)]

    visited = [[False] * N for _ in range(N)]

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    cores = []
    total_wire = float('inf')
    
    for r in range(N):
        for c in range(N):
            if init[r][c] == 1 and r != 0 and r != N - 1 and c != 0 and c != N - 1:
                cores.append((r, c))
    
    dfs(1, 0)

    print(f'#{tc} {total_wire}')
    