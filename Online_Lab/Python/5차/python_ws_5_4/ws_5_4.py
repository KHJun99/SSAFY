# 아래 함수를 수정하시오.
# 1번째 코드
# def capitalize_words(s):
    
    # 입력 받은 문자열을 문자로 분리하여 새로운 리스트 생성
    # 기준을 ', '로 잡은 이유 world!앞에 빈칸으로 인해 capitalize()가 되지 않기 때문 
    # word_list = list(s.split(', '))         
    # result_lst = []

    # for i in word_list:
    #     result_lst.append(i.capitalize())
        
    # return ', '.join(result_lst)

# 2번째 코드
def capitalize_words(s):
    word_list = list(s.split(','))

    # 문자열 capitalize() 실행
    for i in range(len(word_list)):
        # strip()를 하는 이유 : 여백으로 인해 두번째 이상 단어가 capitalize() 되지 않기 때문
        word_list[i] = word_list[i].strip().capitalize()

    return ', '.join(word_list)

result = capitalize_words("hello, world!")
print(result)
