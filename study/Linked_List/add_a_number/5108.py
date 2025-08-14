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
        self.val = val  # 현재 노드의 값
        self.next = None  # 다음 노드를 가리키는 포인터


def add_after(head, idx, val):
    """연결 리스트의 idx 위치에 새 값 val을 삽입하고 head 반환"""
    new_node = Node(val)

    # 0번 인덱스에 삽입 (맨 앞 삽입)
    if idx == 0:
        new_node.next = head
        return new_node

    # 삽입할 위치 직전까지 이동
    cur = head
    for _ in range(idx - 1):    # 삽입할 위치의 바로 앞 노드까지 이동하기 위해 -1
        if cur.next is None:  # 리스트 길이보다 idx가 크면 마지막에 삽입
            break
        cur = cur.next

    # 새 노드를 현재 노드 뒤에 연결
    new_node.next = cur.next
    cur.next = new_node
    return head


T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())  # N: 초기 길이, M: 삽입 횟수, L: 출력할 인덱스
    arr = list(map(int, input().split()))  # 초기 값들

    # 연결 리스트 생성
    head_node = None
    if arr:  # arr가 비어있지 않은 경우
        head_node = Node(arr[0])
        cur = head_node
        for i in range(1, len(arr)):
            cur.next = Node(arr[i])     # 최신 링크필드를 다음 노드랑 연결
            cur = cur.next

    # M번 삽입 작업
    for _ in range(M):
        idx, data = map(int, input().split())
        head_node = add_after(head_node, idx, data)

    # L번째 노드 값 찾기
    cur = head_node
    for _ in range(L):
        if cur is None:  # 인덱스가 범위를 벗어나면 중단
            break
        cur = cur.next

    # 결과 출력 (노드가 없으면 -1)
    print(f'#{tc} {cur.val if cur else -1}')
