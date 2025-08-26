# 아래 함수를 수정하시오.
def union_sets(set1, set2):
    return set1.union(set2)

def union_multiple_sets(*sets):
    if len(sets) < 2:
        print('최소 두 개의 셋이 필요합니다.')
        return set()        # 일관성 및 안정성을 위해 빈 집합 반환
    
    result_sets = set()

    for s in sets:
        result_sets |= s
    
    return result_sets


result = union_sets({1, 2, 3}, {3, 4, 5})
print(result)  # {1, 2, 3, 4, 5}

result = union_multiple_sets({1, 2}, {3, 4}, {5, 6})
print(result)  # {1, 2, 3, 4, 5, 6}

result = union_multiple_sets({1, 2})
# 출력 : 최소 두 개의 셋이 필요합니다
