# [파이썬 S/W 문제해결 기본] 8일차 - 이진탐색 (D2)
"""
문제 상황

- 1부터 N까지의 자연수를 **이진 탐색 트리(BST)**에 저장해야 한다.
- 이때 트리는 완전 이진 트리 형태로 만들어진다.
- 이진 탐색 트리 규칙:
    - 왼쪽 서브트리 루트 값 < 현재 노드 값 < 오른쪽 서브트리 루트 값
"""
import sys
sys.stdin = open('5176_input.txt')


def inorder(tree, i, out):
    if i > len(tree) - 1:
        return

    inorder(tree, i * 2, out)
    out.append(i)
    inorder(tree, i * 2 + 1, out)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    bt = []
    for i in range(N + 1):
        bt.append(i)

    ino = []
    tree = [0] * (N + 1)
    inorder(tree, 1, ino)

    for i in range(1, N + 1):
        tree[ino[i - 1]] = i

    print(f'#{tc} {tree[1]} {tree[N//2]}')
