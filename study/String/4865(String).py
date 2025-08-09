t = int(input())

# 테스트 케이스 만큼 반복
for i in range(1, t + 1):
    str1 = input()
    str2 = input()
    
    # 글자 개수 리스트
    count_lst = list()
    
    # str1 알파벳 비교
    # set()으로 중복 제거
    for j in set(str1):
        # 개수 카운트
        match = str2.count(j)
        count_lst.append(match)
    
    print(f'#{i} {max(count_lst)}')    
        