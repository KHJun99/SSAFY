# [S/W 문제해결 기본] 9일차 - 중위순회

import sys
sys.stdin = open('input.txt')


def inorder(N, L, out):
    # L이 범위를 벗어나면 종료
    if L > N:
        return
    # 왼쪽 -> 현재 -> 오른쪽
    inorder(N, L * 2, out)
    out.append(L)           # 노드 '번호'만 담는다 (이후 문자로 변환)
    inorder(N, L * 2 + 1, out)


T = 10
for tc in range(1, T + 1):
    N = int(input())

    # 1) 입력으로부터 "인덱스 -> 문자" 매핑 구성
    #    각 줄: "번호 문자 [왼][오]" 형태가 될 수 있지만, 여기서는 번호와 문자만 쓰면 됨
    val = [''] * (N + 1)    # val[i] == i번 노드의 문자
    for _ in range(N):
        parts = input().split()
        idx = int(parts[0])
        ch = parts[1]
        val[idx] = ch

    # 2) 중위순회로 '노드 번호' 순서를 얻는다
    order = []
    inorder(N, 1, order)    # order에는 [노드번호, 노드번호, ...] 가 들어감

    # 3) 번호를 문자로 변환해서 결과 생성
    res = [val[i] for i in order]

    # 출력 (문자열로 이어 붙이거나, 리스트 그대로 보고 싶으면 그대로 출력)
    print(f'#{tc}', ''.join(res))





