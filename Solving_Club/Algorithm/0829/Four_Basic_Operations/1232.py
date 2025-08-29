# [S/W 문제해결 기본] 9일차 - 사칙연산 (D4)
"""
문제 상황

- 사칙연산으로 구성된 수식을 **이진 트리(Expression Tree)**로 표현할 수 있다.
- 예: 식 "(9 / (6 - 4)) * 3" → 이진 트리 형태로 변환 가능.

markdown
코드 복사
        *
      /   \
     /     3
    /
   /
   ÷
  / \
 9   -
    / \
   6   4

트리 규칙

- 연산자(+, -, *, /)는 내부 노드(부모 노드)에 위치한다.
- 피연산자(정수)는 리프 노드(말단 노드)에 위치한다.
- 각 연산자는 자신의 왼쪽 서브트리와 오른쪽 서브트리 결과를 계산하여 적용한다.

요구사항

- 주어진 이진 트리가 사칙연산 식을 나타낼 때, 이를 계산한 결과를 출력하는 프로그램을 작성한다.
- 계산 도중의 모든 연산은 실수 연산(float) 으로 처리한다.
"""
import sys
sys.stdin = open('input.txt')

class node():
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right

def inorder(now, out):
    if bt[now].left:
        inorder(bt[now].left, out)
    out.append(bt[now].key)
    if bt[now].right:
        inorder(bt[now].right, out)


T = 10
for tc in range(1, T + 1):
    N = int(input())

    cacu = [0] * (N + 1)
    bt = {}
    for _ in range(N):
        arr = list(map(str, input().split()))
        if arr[1] in '-+*/':
            bt[arr[0]] = node(arr[0], arr[2], arr[3])
        else:
            bt[arr[0]] = node(arr[0], None, None)
        cacu[int(arr[0])] = arr[1]

    ino = []
    inorder('1', ino)
    ino = list(map(int, ino))

    print(ino)
    print(cacu)
    exit()