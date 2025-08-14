# [파이썬 S/W 문제해결 기본] 7일차 - 수열 합치기

"""
문제

1. 주어진 수열과 추가하는 수열의 첫자리를 비교하여 첫자리 보다 큰 숫자 앞에 추가
2. 큰 숫자가 없을 경우 맨뒤에 추가
3. 마지막 수열까지 합친 후, 맨 뒤에 숫자부터 역순으로 10개 출력

N : 수열의 길이
M : 수열의 개수
"""
import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # 합쳐질 수열 arr (양의 무한대)
    arr = [float('inf')]
    cnt = 0     # 현재까지 합쳐진 수열 개수
    for _ in range(M):
        a = list(map(int, input().split()))
        for i in range(N * cnt + 1):
            if a[0] < arr[i]:
                arr[i:i] = a        # i 위치에 새 수열 a 전체를 통째로 삽입
                break
        cnt += 1    #합쳐진 수열 개수 증가
    print(f'#{tc}', *arr[-11:-1][::-1])       # arr[-11:-1] 10개 선택



# class Node():
#     def __init__(self, val):
#         self.val = val
#         self.prev = None
#         self.next = None
#
#
# T = int(input())
# for tc in range(1, T + 1):
#     N, M = map(int, input().split())
#     heads = []
#     tails = []
#     for i in range(M):
#         seq = list(map(int, input().split()))
#
#         # 연결 리스트 생성
#         head_node = None
#         if seq:  # seq가 비어있지 않은 경우
#             head_node = Node(seq[0])
#             cur = head_node
#             for i in range(1, len(seq)):
#                 cur.next = Node(seq[i])  # 최신 링크필드를 다음 노드랑 연결
#                 cur = cur.next
#             if cur.next == None:
#                 tails.append(cur.val)
#             heads.append(head_node.val)
#
#         for j in range(1, M):
#             if heads[i + 1] < seq[j]:
#                 pass