# [파이썬 S/W 문제해결 구현] 3일차 - 컨테이너 운반 (D3)
"""
문제
- 화물이 실려있는 N개의 컨테이너를 M대의 트럭으로 A도시에서 B도시로 운반하려 한다.
- 트럭당 한 개의 컨테이너 운반 가능, 트럭의 적재용량을 초과하는 컨테이너는 운반 불가능
- A도에서 B도시로 최대 M대의 트럭이 편도로 한번 만 운행
- 이동한 화물의 총 중량이 최대가 되도록 컨테이너를 옮겼다면, 옮겨진 화물의 전체 무게를 출력
- 컨테이너를 한 개도 옮길 수 없는 경우 0 출력

입력
- 첫 줄에 테스트 케이스의 수 T 주어진다.
- 다음 줄부터 테스트 케이스 별로 컨테이너 수 N과 트럭 수 M이 주어진다.
- 다음 줄에 N개의 화물이 무게 wi
- 다음 줄에 M개의 트럭의 적재용량 ti
- 1 <= N, M <= 100, 1 <= wi, ti <= 50
"""
import sys
sys.stdin = open('5201_input.txt', 'r')


# 반복문 사용
# def max_load(cw, tw):
#     i = j = 0        # i: 컨테이너, j: 트럭
#     total = 0
#
#     #  1) 두 포인터 스캔
#     while i < len(cw) and j < len(tw):
#         if cw[i] <= tw[j]:      # 이 트럭이 이 컨테이너를 실을 수 있으면
#             total += cw[i]
#             i += 1
#             j += 1              # 둘 다 다음으로
#         else:
#             i += 1              # 더 가벼운 컨테이너를 찾는다
#
#     return total


# 재귀사용
def trans(ci, tj, cw, tw):
    # ci: 컨테이너 인덱스, tj: 트럭 인덱스
    if ci == len(cw) or tj == len(tw):
        return 0
    if cw[ci] <= tw[tj]:
        # 싣는다: 둘 다 다음
        return cw[ci] + trans(ci + 1, tj + 1, cw, tw)
    else:
        # 못 싣는다: 더 가벼운 컨테이너로
        return trans(ci + 1, tj, cw, tw)


T = int(input().strip())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # wi : 화물의 무게, ti : 트럭의 적재용량
    wi = list(map(int, input().split()))
    ti = list(map(int, input().split()))

    wi.sort(reverse=True)
    ti.sort(reverse=True)

    print(f'#{tc} {trans(0, 0, wi, ti)}')       # 재귀 출력
    # print(f'#{tc} {max_load(wi, ti)}')        # 반복문 출력
