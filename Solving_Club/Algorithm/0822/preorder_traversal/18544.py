# 연습문제 1. 전위 순회
"""
문제
첫 줄에는 트리의 정점의 총 수 V가 주어진다. 그 다음 줄에는 V-1개 간선이 나열된다.
간선은 그것을 이루는 두 정점으로 표기된다. 간선은 항상 “부모 자식” 순서로 표기된다.
아래 예에서 두 번째 줄 처음 1과 2는 정점 1과 2를 잇는 간선을 의미하며 1이 부모, 2가 자식을 의미한다.
간선은 부모 정점 번호가 작은 것부터 나열되고, 부모 정점이 동일하다면 자식 정점 번호가 작은 것부터 나열된다.

다음 이진 트리 표현에 대하여 전위 순회하여 정점의 번호를 출력하시오.

전위순회 수행 방법
1. 현재 노드 n을 방문하여 처리
2. 현재 노드 n의 왼쪽 서브트리로 이동
3. 현재 노드 n의 오른쪽 서브트리로 이동
"""
import sys
sys.stdin = open('input.txt')
from collections import deque

N = int(input())
arr = list(map(int, input().split()))

bt = [[] for _ in range(N + 1)]
for parents, child in zip(arr[0::2], arr[1::2]):
    bt[parents].append(child)

