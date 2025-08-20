# [파이썬 S/W 문제해결 기본] 8일차 - 이진 탐색

"""
문제
1부터 N까지의 자연수를 이진 탐색 트리에 저장하려고 한다.
이진 탐색 트리는 어떤 경우에도 저장된 값이 왼쪽 서브트리의 루트 <현재 노드 <오른쪽 서브 트리의 루트인 규칙을 만족한다.
완전 이진 트리의 노드 번호는 루트를 1번으로 하고 아래로 내려가면서 왼쪽에서 오른쪽 순으로 증가한다.
N이 주어졌을 때 완전 이진 트리로 만든 이진 탐색 트리의 루트에 저장된 값과, N/2번 노드(N이 홀수인 경우 소수점 버림)에 저장된 값을 출력하는 프로그램을 만드시오.

접근 방법
1. 중위 순회 순서를 구한다.
2. 순서에 맞춰 1부터 값 삽입
"""
import sys
sys.stdin = open('sample_input.txt')

# 중위 순회 함수
def inorder_arr(tree, i, out):
    # 범위 밖이거나 비어있으면 종료
    if i >= len(tree) or tree[i] is None:
        return
    # 왼쪽 서브트리 방문
    inorder_arr(tree, 2*i, out)
    # 현재 노드 방문
    out.append(tree[i])
    # 오른쪽 서브트리 방문
    inorder_arr(tree, 2*i+1, out)


T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    # N번 인덱스까지 노드가 있는 완전 이진 트리를 가정
    # 값 = 인덱스가 되도록 반복문
    bt = []
    for i in range(N + 1):
        bt.append(i)

    # 중위 순회 결과를 담을 리스트
    res = []
    inorder_arr(bt, 1, res)     # 루트(1)에서 시작
    # 예제 1 res : 4, 2, 5, 1, 6, 3

    # inorder_lst[idx] = 해당 노드(idx)의 중위 순서
    inorder_lst = [0] * (N + 1)

    for k, idx in enumerate(res, start=1):
        inorder_lst[idx] = k
        # idx, k / 4, 1 / 2, 2 / 5, 3 / 1, 4 / 6, 5 / 3, 6

    print(f'#{tc} {inorder_lst[1]} {inorder_lst[N // 2]}')
