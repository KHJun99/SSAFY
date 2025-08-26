# 아래에 코드를 작성하시오.
class Myth:
    type_of_myth = 0
    
    # 생성자 메서드
    def __init__(self, name):
        self.name = name
        print(name)
        Myth.increase_myth()
    
    @classmethod
    def increase_myth(cls):
        cls.type_of_myth += 1

    @staticmethod
    def description():
        print('신화는 한 나라 혹은 한 민족으로부터 전승되어 오는 예로부터 섬기는 신을 둘러싼 이야기를 뜻한다.')
               

person1 = Myth('dangun')
person2 = Myth('greek & rome')
print(f'현재까지 생성된 신화 수 : {Myth.type_of_myth}')
Myth.description()