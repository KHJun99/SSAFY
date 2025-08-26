# 아래 함수를 수정하시오.
def remove_duplicates(s):
    new_lst = []
    for num in s:

        # 입력 받은 리스트 s가 새로운 리스트(new_lst)에 없으면 추가
        if num not in new_lst:
            new_lst.append(num)

    return new_lst


result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)
