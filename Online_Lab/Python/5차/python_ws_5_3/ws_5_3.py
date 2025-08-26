# 아래 함수를 수정하시오.
def sort_tuple(s):
    new_list = list(s)
    new_list.sort()
    return tuple(new_list)


result = sort_tuple((5, 2, 8, 1, 3))
print(result)
