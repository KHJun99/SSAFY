# [파이썬 S/W 문제해결 기본] 8일차 - 이진 힙
"""
문제
1000000이하인 N개의 서로 다른 자연수가 주어지면 입력 순서대로 이진 최소힙에 저장하고, 마지막 노드의 조상 노드에 저장된 정수의 합을 알아내는 프로그램을 작성

조건
1. 항상 완전 이진 트리를 유지하기 위해 마지막 노드 뒤에 새 노드를 추가
2. 부모 노드의 값 < 자식 노드의 값을 유지, 새로 추가된 노드의 값이 조건에 맞지 않는 경우, 조건을 만족할 떄까지 부모 노드와 값을 바꾼다.
3. 노드 번호는 루트가 1번, 왼쪽에서 오른쪽으로, 더 이상 오른쪽이 없는 경우 다음 줄로 1씩 증가

관련 개념
- 최소 힙 : 키 값이 가장 작은 노드를 찾기 위한 완전 이진 트리
  1. 부모 노드의 키값 < 자식 노드의 키값
  2. 루트 노드 : 키 값이 가장 작은 노드

"""
import sys
sys.stdin = open('sample_input.txt')


def min_heap(tree, val):
    # tree[1] = min(val)
    # # # 루트 노드에 최소 값을 고정해주었기 때문에 val 리스트에서 최소값 삭제
    # val.remove(min(val))
    while True:
        for i in range(1, len(tree)):
            tree[i] = val[0]
            val.pop(0)
            while i > 0 and tree[i] < tree[i // 2]:
                tree[i], tree[i // 2] = tree[i // 2], tree[i]
                i //= 2
        if len(val) == 0:
            break

    return tree


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    val = list(map(int, input().split()))

    bt = [0] * (N + 1)
    heap = min_heap(bt, val)

    parent = N // 2
    result = 0
    while parent > 0:
        result += heap[parent]
        parent //= 2

    print(f'#{tc} {result}')
