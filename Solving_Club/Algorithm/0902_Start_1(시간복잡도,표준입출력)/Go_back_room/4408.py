# 자기 방으로 돌아기기 (D4)
"""
구현 방법
1. 400개의 2차원 리스트(방)(현재, 돌아가야하는 방) 만들기
2. 현재 방 ~ 돌아갈 방 사이에 다른 친구의 현재 방이 위치하면 같이 이동 불가능
3. 이동 할 때 마다 time + 1 (동시에 이동 가능)
"""
import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())        # 돌아가야 할 학생들의 수
    corridor = [0] * 201
    for room in range(N):
        cur, nxt = map(int, input().split())
        if cur > nxt:
            cur, nxt = nxt, cur

        cur = (cur + 1) // 2
        nxt = (nxt + 1) // 2

        for i in range(cur, nxt + 1):
            corridor[i] += 1
    result = max(corridor)
    print(f'#{tc} {result}')