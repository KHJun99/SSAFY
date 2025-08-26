def restructure_word(word, arr):
    for i in word:
        # i가 정수이면 True
        if i.isdecimal() == True:
            # 위 조건을 만족하면 pop() i 번 실행
            for _ in range(int(i)):
                arr.pop()
        else:
            # i가 정수가 아닌 경우
            arr.remove(i)

    return arr


original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
arr = []

# 슬라이싱을 통해 extend 사용
arr.extend(original_word[ : ])

print(arr)

result = restructure_word(word, arr)

# result 출력
print(result)

# result 하나의 문자열로 변환하여 출력
print(''.join(result))
