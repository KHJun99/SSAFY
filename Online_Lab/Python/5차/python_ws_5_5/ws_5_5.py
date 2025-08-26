# 아래 함수를 수정하시오.
def even_elements(lst):
    new_number = []
    new_lst = []

    for num in lst:
        # 짝수 확인 조건문
        if num % 2 == 0:
            # pop메소드를 이용하여 기존 리스트에서 제거 후 해당 값 반환
            idx = lst.pop(lst.index(num))
            new_number.append(idx)

    # 선별된 new_number(짝수)를 새로운 리스트에 추가
    new_lst.extend(new_number)
    return new_lst


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
