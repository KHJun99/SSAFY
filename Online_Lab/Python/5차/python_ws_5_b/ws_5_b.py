data_1 = 'qweqwYadnOyjnsaU4trwg asjnaAn245krRmkfE 42grTasdnHasdnvEasdn asdevadnBasdanEsdkqefqefvaSasdqaeeqqvedwt5hfbsdT24tewfd'
'''
예시코드
arr = [1, 2, 3, 4, 5]
for num in arr:
    print(num, end='')
출력결과 : 12345
'''
# 아래에 코드를 작성하시오.
for word in data_1:
    if word.isupper() == True or word == ' ':
        print(word, end = "")

print()
data_2 = '걉파반샤팝다푸거맥파바자들퍼바배들밥샵파누타히매니배사바파힘다브사부힙헤베내테치대내'
arr = []
# 아래에 코드를 작성하시오.

standard = ['내', '힘', '들', '다']
for word in standard:
    # 인덱스 찾는 과정
    idx = data_2.find(word)

    # standard 리스트 내의 글자가 data_2에 없으면 -1을 반환하기 때문
    if idx != -1:
        arr.append(idx)

# 기존 arr 출력
print(arr)

# 오름차순으로 정렬
arr.sort()

# 정렬된 arr 출력
print(arr)

# 정련된 arr 인덱스에 맞는 단어 출력
for idx in arr:
    print(data_2[idx], end = '')