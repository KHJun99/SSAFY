# 백준_10775_공항 (G2)
"""
## [문제 정리]
- 공항에는 G개의 게이트가 존재 (1 ~ G번)
- 공항에는 P개의 비행기가 순서대로 도착 예정
    - i번째 비행기를 1번부터 gi번째 게이트 중 하나에 영구적으로 도킹
    - 비행기가 어느 게이트에도 도킹할 수 없다면 공항은 폐쇄
    - 비행기 도착 불가능
- 공항에 도킹시킬 수 있는 최대 비행기 수를 구하여라.
"""
import sys
input = sys.stdin.readline

def find(x):
    while parent[x] != x:               # 루트가 아닐 동안
        parent[x] = parent[parent[x]]   # 경로 압축
        x = parent[x]                   # 부모로 이동
    return x                            # 루트 반환


G = int(input())
P = int(input())

parent = list(range(G + 1))     # 초기화

ap = 0

for _ in range(P):
    gi = int(input())
    gate = find(gi)                     # 가장 큰 게이트 찾기

    if gate == 0:                       # 0번 게이트 -> 도킹 불가능 -> 종료
        break

    parent[gate] = find(gate - 1)       #  gate - 1 번 게이트와 연결 (중복 도킹 불가능 하기 때문)

    ap += 1

print(ap)


# 시간초과
# G = int(input())
# P = int(input())
# gate = [0] + [int(input()) for _ in range(P)]
#
# docking = [False] * (G + 1)
# ap = 0
# count = 0
#
# for i in range(1, P + 1):
#     count += 1
#     idx = gate[i]
#     for j in range(idx, 0, -1):
#         if not docking[j]:
#             docking[j] = True
#             ap += 1
#             break
#     if ap != count:
#         break
# print(ap)
#-----------------------------------------------------
