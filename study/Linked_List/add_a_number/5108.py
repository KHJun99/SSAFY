# [파이선 S/W 문제해결 기본] 7일차 - 숫자 추가
"""
문제 설명 : M개의 숫자를 지정된 위치에 추가하면 완성
"""
"""
1. 주어진 수열을 연결 리스트로 변환
2. 노드와 헤드를 이용하여 추가
N : 수열의 길이
M : 추가 횟수 (인덱스, 번호)
L : 출력할 인덱스 번호
"""
import sys
sys.stdin = open('sample_input.txt')

class Node:
    def __init__(self, val):
        self.val = val    # 현재 노드의 값
        self.next = None    # 다음 노드를 가리키는 포인터


def add_after(self, node, val):
    new_node = Node(val)
    new_node.next = node.next
    node.next = new_node


T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    arr = list(map(int, input().split()))

    # 입력 받은 수열을 연결 리스트로 변환
    if not arr:
        head_node = None
    else:
        head_node = Node(arr[0])
        cur = head_node
        for i in range(1, len(arr)):
            cur.next = Node(arr[i])
            cur = cur.next

    for _ in range(M):
        idx, data = map(int, input().split())

    # print(f'#{tc} {}')