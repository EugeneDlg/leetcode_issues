input_number = int(input("Enter a number: "))


def is_palindrome_bf(input_number):
    lst = []
    quotient = input_number
    while quotient > 0:
        lst.append(quotient % 10)
        quotient = int( quotient / 10)
    return lst == lst[::-1]


def is_palindrome2(number):
    if number < 0 or number%10==0 and number!=0:
        return False
    original_number = number
    r = 0
    while number > r:
        r = r * 10 + number % 10
        number = int(number / 10)
    return r, r==number or int(r/10)==number



print(is_palindrome2(input_number))
# print(is_palindrome_bf(input_number))

