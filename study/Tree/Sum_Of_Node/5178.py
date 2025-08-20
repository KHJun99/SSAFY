# [파이썬 S/W 문제해결 기본] 8일차 - 노드의 합 (D3)

"""
문제
완전 이진 트리의 리프 노드에 1000이하의 자연수가 저장되어 있고, 리프 노드를 제외한 노드에는 자식 노드에 저장된 값의 합이 들어있다고 한다.
다음은 리프 노드에 저장된 1, 2, 3이 주어졌을 때, 나머지 노드에 자식 노드의 합을 저장한 예이다.
루트가 1번, 같은 단계에서는 왼쪽에서 오른쪽으로 증가, 단계가 꽉 차면 다음 단계의 왼쪽부터 시작
완전 이진 트리의 특성상 1번부터 N번까지 빠지는 노드 번호는 없다.
리드 노드의 번호와 저장된 값이 주어지면 나머지 노드에 자식 노드 값의 함을 저장한 다음, 지정 한 노드 번호에 지정된 값을 출력
"""
import sys
sys.stdin = open('sample_input.txt')

def find_node_val(tree, L, N):
    # 범위 밖이면 0
    if L > N:
        return 0
    # 리프(자식 없음)이면 현재 값 반환
    if L * 2 > N:
        return tree[L]
    # 내부 노드: 자식 합으로 채움
    left = find_node_val(tree, L * 2, N)
    right = find_node_val(tree, L * 2 + 1, N)
    tree[L] = left + right
    return tree[L]


T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    bt = [0] * (N + 1)  # 0으로 초기화
    for _ in range(M):
        idx, val = map(int, input().split())
        bt[idx] = val

    result = find_node_val(bt, L, N)
    print(f'#{tc} {result}')

