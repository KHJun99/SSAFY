# 백준_7568_덩치 (s5)
"""
핵심 요약
- 사람의 키와 몸무게로 "덩치"를 정의하고, 집단 내에서 더 큰 덩치를 가진 사람의 수를 기준으로 등수를 매기는 문제.

[구조적 분석]
1. 문제 정의
- 각 사람의 덩치는 (몸무게, 키) 쌍으로 표현됨.
- 덩치 비교: 두 값(몸무게, 키)이 모두 커야 더 큰 덩치라고 판정.
- 등수 산정: 자신보다 큰 덩치가 k명 있으면 등수는 k+1.

2. 원인 분석
- 단순 정렬 불가: 키와 몸무게가 교차되는 경우(한쪽은 크고, 한쪽은 작음)에는 크기 비교 불가능.
- 따라서 모든 사람을 서로 비교해야 함.

3. 해결 방안
- 모든 사람 쌍을 비교한다.
- 자기보다 큰 덩치가 몇 명 있는지 센다.
- 그 수에 1을 더해 등수를 매긴다.

4. 요약 포인트
- 덩치 = (몸무게, 키)
- 비교 기준 = 두 값 모두 커야 "더 크다"
- 등수 = 자기보다 큰 덩치의 수 + 1
- 같은 등수를 가진 사람 가능
"""
N = int(input())
physical = []

for _ in range(N):
    weight, height = map(int, input().split())
    physical.append([weight, height])

rank = []
count = 1

# 맨 앞 요소 뒤로 보내는 반복문
for i in range(N):
    # 각 요소들을 비교하는 반복문
    for j in range(N - 1):
        if physical[0][0] < physical[j + 1][0] and physical[0][1] < physical[j + 1][1]:
            count += 1
    rank.append(count)
    count = 1
    physical.append(physical.pop(0))

print(*rank)