# [파이썬 S/W 문제해결 기본] 6일차 - 노드의 거리
import sys
sys.stdin = open('sample_input.txt')

# T : 테스트 케이스 개수
# V : 노드 개수, E : 간선 정보
# node1, node2 : 간선의 양쪽 노드 번호
# S, G : 축발 노드, 도착 노드
T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    node1, node2 = [list(map(int, input().split())) for _ in range(E)]
    S, G = map(int, input())

