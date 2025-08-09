t = int(input())

for order in range(1, t + 1):
    pattern = input()
    string = input()
    pattern_length = len(pattern)
    string_length = len(string)
    
    # 인덱스 변수, 매칭 변수 선언
    idx  = 0
    is_match = 0
    while True:
        # 슬라이싱 end 값 선언
        length = idx + pattern_length
        
        # 문자열 0번째 인덱스부터 패턴 찾기
        if string[idx:length] != pattern:
            idx += 1
            # 문자열 크기 - 슬라이싱 start 값이 비교문자 길이보다 길 경우
            # 비교문자 존재 X
            # while문 정지
            if idx > (string_length - pattern_length):
                print(f'#{order} {is_match}')
                break    
        else:
            is_match += 1
            print(f'#{order} {is_match}')
            break

            
            
    
