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
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


G = int(input())
P = int(input())

parent = list(range(G + 1))     # 초기화

ap = 0

for _ in range(P):
    gi = int(input())
    gate = find(gi)
    if gate == 0:
        break
    ap += 1
    parent[gate] = find(gate - 1)

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
