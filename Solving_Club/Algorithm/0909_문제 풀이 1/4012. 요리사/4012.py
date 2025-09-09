# [모의 SW 역량테스트] 요리사
"""
문제
- 두 명의 손님에게 음식을 제공한다.
- 두 명의 손님은 식성이 비슷하기 때문에, 최대한 비슷한 맛의 음식을 제공
- N개의 식재료
- N / 2씩 나누어 두 개의 요리 조리 (N 은 짝수)
- 비슷한 맛의 음식을 만들기 위해서는 A음식과 B음식의 맛의 차이가 최소가 되도록 재료를 분배해야 한다.
- 음식의 맛은 음식을 구성하는 식재료들의 조합에 따라 변화
- 식재료 i는 식재로 j와 같이 요리하게 되면 궁합이 잘 맞아 시너지 Sij 발생
"""
import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    synergy = [list(map(int, input().split())) for _ in range(N)]

    