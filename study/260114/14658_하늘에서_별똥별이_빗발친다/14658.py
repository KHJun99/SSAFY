# 백준_14658_하늘에서_별똥별이_빗발친다 (G3)
"""
## [문제 정리]

- 목적 : 지표면에 떨어지는 별똥별의 수를 최소화
- 트램펄린 크기 : L * L
- 별똥별이 떨어지는 위치는 알고 있다.
- 트램펄린으로 최대한 많은 별동별을 우주로 튕겨낼 계획
- 트램펄린 구매 예산 심의 통과 존재
- 별똥별이 떨어지는 위치는 겹치지 않는다.
- 별동별이 트램펄린 모서리에 무딪혀도 팅겨나간다.
- 트램펄린은 비스듬하게 배치할 수 없다.

- 최대한 많은 별똥별을 튕겨내도록 트램펄린을 배치했을 때, 지구에 부딪히는 별똥별의 개수를 구하시오.
"""
def check(length, star_lst):
    global result

    for i in range(K):
        for j in range(K):
            tx = star_lst[i][0]
            ty = star_lst[j][1]

            count = 0
            for sx, sy in star_lst:
                if tx <= sx <= tx + length and ty <= sy <= ty + length:
                    count += 1

            result = max(result, count)


""" 변수 설명
N : 별똥별이 떨어지는 구역의 가로 길이
M : 별똥별`이 떨어지는 구역의 세로 길이
L : 트램펄린의 한 변의 길이
K : 별똥별의 수
"""
N, M, L, K = map(int, input().split())
starts = [list(map(int, input().split())) for _ in range(K)]

result = 0

check(L, starts)

print(K - result)