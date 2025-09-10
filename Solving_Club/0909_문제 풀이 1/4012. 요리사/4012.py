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
"""
재료는 총 N개
음식별 재료는 N//2만큼 뽑아서 요리를 진행 (조합)
    - 재료를 뽑는 순서는 상관 없음 => 순열 x

음식 재료 N//2 중에서 2개씩 요리
    - 재료를 뽑는 순서는 상관 없음 => 순열 x (조합)
- 해당 재료를 뽑아서 요리를 했을 때의 총합을 구해서
- A와 B의 차이를 계산하고
- 최소값을 찾으면 끝
"""
# target : 뽑으려는 원래 리소스
# r : 몇 개를 뽑아야 하는지 선택하는 값
# choice : 현재 봅은 요소가 들어 있는 리스트
# start : 뽑는 요소의 인덱스 정보를 갱신 --> 없으면 순열 코드
# [(1, 2), (1, 3), (1, 4), ...., (3, 4)]

def combination(target, r, choice, start):
    result = []                 # combination의 반환 값
    if len(choice) == r:      # 뽑은 갯수가 목표하는 개수와 동일하면 종료
        result.append(choice[:])        # choice가 주소이기 때문에 원본이 바뀌면 append 된 choice 값도 같이 변경
        return result

    for idx in range(start, len(target)):          # 뽑은 것을 다시 선택하지 않도록 범위 조정
        choice.append(target[idx])          # 현재 값을 선택
        result += combination(target, r, choice, idx + 1)      # idx를 선택했으니 다음 자리부터 다음 요소를 뽑으러 재귀 호출
        choice.pop()                        # 다른 선택을 위해 현재 선택된 값을 제거

    return result


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]

    min_value = float('inf')
    # 모든 재료에서 절반을 선택한 모든 조합
    ingredient_a_list = combination(list(range(N)), N//2, [], 0)

    # 절반의 조합 리스트에서 하나씩 조합을 꺼내 계산을 진행
    for ingredient_a in ingredient_a_list:
        # b의 재료는 모든 재료에서 a의 재료를 제와한 재료
        # ingredient_b = [ingred for ingred in list(range(N)) if ingred not in ingredient_a]
        ingredient_b = list(set(range(N)) - set(ingredient_a))

        # 뽑은 재료에서 2개씩 뽑아 요리를 진행
        synergy_a = 0
        for i, j in combination(ingredient_a, 2, [], 0):
            synergy_a += S[i][j] + S[j][i]

        synergy_b = 0
        for i, j in combination(ingredient_b, 2, [], 0):
            synergy_b += S[i][j] + S[j][i]

        min_value = min(min_value, abs(synergy_a - synergy_b))

    print(f'#{tc} {min_value}')