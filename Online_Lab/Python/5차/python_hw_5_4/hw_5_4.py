# 아래 함수를 수정하시오.
def find_min_max(lst):
    max = 0
    min = lst[0]
    for i in lst:
        if i > max:
            max = i
        if i < min:
            min = i
    return tuple((min, max))


result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)
