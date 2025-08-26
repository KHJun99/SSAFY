import requests
from pprint import pprint as print

censored_user_list = {}
def create_user(user_lst):
    for i in user_lst:
        name = user_lst[i]
        company = user_lst[i][1]
        censored_user_list = {
            name : [company]
        }
    return censored_user_list


def censorship(company, name):
    for i in black_list:
        if company == i:
            print(f'{company} 소속의 {name} 은/는 등록할 수 없습니다.')
            return False
        else:
            print('이상 없습니다.')
            return True


API_URL = 'https://jsonplaceholder.typicode.com/users'

for i in range(10):
    response = requests.get(API_URL).json()

    user_name = response[i]['username']
    user_company_name = response[i]['company']['name']
    user_lst = []
    user_info = {
        user_company_name : user_name
    }
    user_lst.append(user_info)
    # user = create_user(user_lst)
    # censorship(user)
print(user_lst[1])


black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]

