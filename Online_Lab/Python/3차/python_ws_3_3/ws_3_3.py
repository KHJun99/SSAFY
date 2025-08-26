def rental_book(name, num_of_books):
    decrease_book(num_of_books)
    return f'{name}님이 {num_of_books}권의 책을 대여하였습니다.'

number_of_book = 100

def decrease_book(num_of_books):
    global number_of_book
    number_of_book -= num_of_books
    return number_of_book

rental_book('홍길동', 3)
print(f'남은 책의 수 : {number_of_book}')
print(rental_book('홍길동', 3))

