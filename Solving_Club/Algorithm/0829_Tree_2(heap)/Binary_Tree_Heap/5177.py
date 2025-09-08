# [파이썬 S/W 문제해결 기본] 8일차 - 이진 힙 (D2)
"""
1. 최소힙(Heap)의 특징

- 완전 이진 트리 유지: 항상 마지막 노드 뒤에 새 노드를 추가한다.
- 부모 ≤ 자식: 부모 노드 값이 자식 노드보다 항상 작거나 같다. 조건을 만족하지 않으면 부모와 값을 교환(swap).
- 노드 번호 부여: 루트는 1번, 왼쪽→오른쪽 순서로 번호를 붙인다.

2. 예시

- 입력: 7, 2, 5, 3, 4, 6
- 결과 트리:
markdown
코드 복사
        2
      /   \
     3     5
    / \   /
   7   4 6

- 마지막 노드(6번)의 조상: 3번, 1번 노드

3. 문제 요구사항

- 서로 다른 자연수들이 입력 순서대로 이진 최소힙에 삽입된다.
- 마지막 노드의 조상 노드에 저장된 정수의 합을 출력하는 프로그램을 작성해야 한다.

👉 핵심: 입력 → 최소힙 생성 → 마지막 노드 조상 추적 → 조상 값 합산
"""
import sys
sys.stdin = open('5177_input.txt')


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    bt = [0] * (N + 1)
    arr = list(map(int, input().split()))

    for i in range(1, N + 1):
        bt[i] = arr[0]
        arr.pop(0)
        # 최소 힙 조건 유지 : 부모보다 값이 작으면 교환
        while i > 0 and bt[i] < bt[i // 2]:
            bt[i], bt[i // 2] = bt[i // 2], bt[i]
            i //= 2

    parents = N // 2
    result = 0
    while bt[parents]:
        result += bt[parents]
        parents //= 2

    print(f'#{tc} {result}')




