data = [
    {
        'name': 'galxy flip',
        'company': 'samsung',
        'is_collapsible': True,
    },
    {
        'name': 'ipad',
        'is_collapsible': False
    },
    {
        'name': 'galxy fold',
        'company': 'samsung',
        'is_collapsible': True
    },
    {
        'name': 'galxy note',
        'company': 'samsung',
        'is_collapsible': False
    },
    {
        'name': 'optimus',
        'is_collapsible': False
    },
]

key_list = ['name', 'company', 'is_collapsible']

# 아래에 코드를 작성하시오.

# data 안의 딕셔너리 갯수 만큼 반복
for i in range(len(data)):
    # 딕셔너리 업데이트를 위한 key 체크
    for j in key_list:
        # key가 없는 경우 'unknown'과 함께 딕셔너리에 추가
        if j not in data[i]:
            data[i].setdefault(j, 'unknown')
    
    for key in key_list:
        print(f'{key}은/는 {data[i].get(key)}입니다.')

    print()