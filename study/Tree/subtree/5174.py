# [파이썬 S/W 문제해결 기본] 8일차 - subtree
"""
문제
주어진 이진 트리에서 노드 N을 루트로 하는 서브 트리에 속한 노드의 개수를 알아내는 프로그램 개발
"""
import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    # E : 간선의 개수, N : 서브트리에서 루트 노드 번호
    E, N = map(int, input().split())
    node_to_node = list(map(int, input().split()))

    # 노드 번호가 1 ~ E + 1번까지 존재하므로 E + 2로 구간 설정
    bt_lst = [[] for _ in range(E + 2)]
    for parent, child in zip(node_to_node[0::2], node_to_node[1::2]):
        bt_lst[parent].append(child)

    # DFS
    node_cnt = 0
    stack = [N]
    while stack:
        cur = stack.pop()
        node_cnt += 1
        # cur의 모든 자식을 스택에 push
        stack.extend(bt_lst[cur])

    print(f'#{tc} {node_cnt}')
