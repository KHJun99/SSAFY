# 아래 함수를 수정하시오.
def reverse_string(s):
    reversed_letters = reversed(s)
    return ''.join(list(reversed_letters))

result = reverse_string("Hello, World!")
print(result)  # !dlroW ,olleH
