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

