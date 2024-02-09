# ***************
# def get_sum(a, b):
#     return a + b
#
# # *************
# from math import log
# def get_log(value, base=2):
#     return log(value, base)

# Функция hide_card()

# def hide_card(card_number):
#     numbers = [ch for ch in card_number.replace(' ', '')]
#
#     for i in range(12):
#         numbers[i] = '*'
#
#     return ''.join(numbers)


# Функция hide_card() (ЧЕРЕЗ FILTER)
# def hide_card(card_number):
#     numbers = list(filter(lambda x: x != ' ', card_number))
#
#     for i in range(12):
#         numbers[i] = '*'
#
#     return ''.join(numbers)


# Функция hide_card()(ОТ ПРЕПОДАВАТЕЛЯ)
# def hide_card(card):
#     return '*' * 12 + card.replace(' ', '')[-4:]


# Функция same_parity()
# def same_parity(numbers):
#     return [el for el in numbers if el % 2 == numbers[0] % 2]

# Функция same_parity()(ОТ ПОЛЬЗОВАТЕЛЯ)
# def same_parity(numbers):
#     return list(filter(lambda x: x % 2 == numbers[0] % 2, numbers))


# Функция is_valid()
#
# def is_valid(pin):
#     if len(pin) < 4 or len(pin) > 6:
#         return False
#     elif not pin.isdigit():
#         return False
#     elif ' ' in pin:
#         return False
#
#     return True

# Функция is_valid()(ОТ ПРЕПОДАВАТЕЛЯ)
# def is_valid(pin):
#     return pin.isdigit() and len(pin) in (4, 5, 6)

# Функция is_valid()(ОТ ПОЛЬЗОВАТЕЛЯ)
# def is_valid(pin: str) -> bool:
#     return all((4 <= len(pin) <= 6, pin.isdigit()))


# Функция print_given()

# def print_given(*args, **kwargs):
#     for el in args:
#         print(el, type(el))
#
#     for key, value in sorted(kwargs.items()):
#         print(f'{key} {value} {type(value)}')


# Функция convert()

# def convert(string):
#     low_list, up_list = [], []
#
#     for ch in string:
#         if ch.isalpha() and ch.isupper():
#             up_list.append(ch)
#         elif ch.isalpha() and ch.islower():
#             low_list.append(ch)
#
#     if len(up_list) > len(low_list):
#         return string.upper()
#     else:
#         return string.lower()


# Функция convert()(ОТ ПРЕПОДАВАТЕЛЯ)
# def convert(string):
#     if sum(1 if c.isupper() else -1 for c in string if c.isalpha()) > 0:
#         return string.upper()
#     return string.lower()

# Функция convert()(ОТ ПРЕПОДАВАТЕЛЯ)
# def convert(text):
#     lower_count = len(list(filter(str.islower, text)))
#     upper_count = len(list(filter(str.isupper, text)))
#     if lower_count >= upper_count:
#         return text.lower()
#     return text.upper()


