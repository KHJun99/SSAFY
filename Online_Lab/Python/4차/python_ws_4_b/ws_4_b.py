food_list = [
    {
        '종류': '한식',
        '이름': '잡채'
    },
    {
        '종류': '채소',
        '이름': '토마토'
    },
    {
        '종류': '중식',
        '이름': '자장면'
    },
]

# 아래에 코드를 작성하시오.
# for 문 코드
# for food in food_list:
#     if food['이름'] == '토마토':
#         food['종류'] = '과일'  # 과일로 변경
#         print(f"{food['이름']} 은/는 {food['종류']}이다.")
#     elif food['이름'] == '자장면':
#         print(f"{food['이름']}엔 고춧가루지")
#     else:
#         print(f"{food['이름']} 은/는 {food['종류']}")
        
# print(food_list)

# while 문 코드
i = 0
while i < len(food_list):
    food = food_list[i]
    if food['이름'] == '토마토':
        food['종류'] = '과일'  # 과일로 변경
        print(f"{food['이름']} 은/는 {food['종류']}이다.")
    elif food['이름'] == '자장면':
        print(f"{food['이름']}엔 고춧가루지")
    else:
        print(f"{food['이름']} 은/는 {food['종류']}")
    
    i += 1
        
print(food_list)