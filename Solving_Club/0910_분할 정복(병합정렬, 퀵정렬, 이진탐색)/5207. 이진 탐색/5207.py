# [파이썬 S/W 문제해결 구현] 4일차 - 이진 탐색 (D3)
"""
문제

- 서로 다른 정수 N개를 오름차순으로 정렬해 리스트 A에 저장.
- 리스트 B의 M개 정수 각각에 대해 이진 탐색으로 A에 존재하는지 확인한다.
- 이때 탐색 과정에서 선택한 구간이 좌/우가 연속으로 같지 않고 번갈아가며 진행되는(= 같은 방향을 두 번 연속 선택하지 않는) 경우만 “조건을 만족”한다고 본다.
- B의 수가 A에 존재하고 탐색 규칙을 지킴(좌·우 연속 금지) 경우의 개수를 구한다.
"""
import sys
sys.stdin = open('5207_input.txt', 'r')


def binary_search(a, b):
    mid = len(a) // 2


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    binary_search(A, B)
    print(f'#{tc} {}')