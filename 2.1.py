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


# Функция filter_anagrams()

# def filter_anagrams(word, *words):
#     return list(filter(lambda x: sorted(x) == sorted(word), *words))

# # word = 'abba'
# # anagrams = ['aabb', 'abcd', 'bbaa', 'dada']
# #
# # print(filter_anagrams(word, anagrams))
# print(filter_anagrams('стекло', []))

# Функция filter_anagrams()(ОТ ПРЕПОДАВАТЕЛЯ)(РАБОТАЕТ БЫСТРЕЕ ЧЕМ ЧЕРЕЗ ЛЯМБДУ)
# def filter_anagrams(word, anagrams):
#     return [anagram for anagram in anagrams if sorted(anagram) == sorted(word)]


# Функция likes()

# def likes(name):
#     if len(name) == 1:
#         return f'{name[0]} оценил(а) данную запись'
#     elif len(name) == 2:
#         return f'{name[0]} и {name[1]} оценили данную запись'
#     elif len(name) == 3:
#         return f'{name[0]}, {name[1]} и {name[2]} оценили данную запись'
#     elif len(name) > 3:
#         return f'{name[0]}, {name[1]} и {len(name) - 2} других оценили данную запись'
#     else:
#         return 'Никто не оценил данную запись'
#
#
# print(likes(['Эндрю', 'Тоби', 'Том', 'Артур']))
#
# # Функция likes()(ОТ ПОЛЬЗОВАТЕЛЯ)
# def likes(v):
#     d = {0: "'Никто не оценил'",
#          1: "f'{v[0]} оценил(а)'",
#          2: "f'{v[0]} и {v[1]} оценили'",
#          3: "f'{v[0]}, {v[1]} и {v[2]} оценили'",
#          4: "f'{v[0]}, {v[1]} и {len(v) - 2} других оценили'"}
#     return eval(d.get(len(v), d[4])) + ' данную запись'
#
# # Функция likes()(ОТ ПОЛЬЗОВАТЕЛЯ)
# def likes(names):
#     l = len(names)
#     match l:
#         case 0:
#             return "Никто не оценил данную запись"
#         case 1:
#             return "{} оценил(а) данную запись".format(*names)
#         case 2:
#             return "{} и {} оценили данную запись".format(*names)
#         case 3:
#             return "{}, {} и {} оценили данную запись".format(*names)
#         case _:
#             return "{}, {} и {} других оценили данную запись".format(*names[:2], l - 2)
#
# # Функция likes()(ОТ ПОЛЬЗОВАТЕЛЯ)
# def likes(s):
#     text = ("'Никто не оценил'",
#             "f'{s[0]} оценил(а)'",
#             "f'{s[0]} и {s[1]} оценили'",
#             "f'{s[0]}, {s[1]} и {s[2]} оценили'",
#             "f'{s[0]}, {s[1]} и {len(s) - 2} других оценили'")[min(4, len(s))]
#     return eval(text) + ' данную запись'


# Функция index_of_nearest()

# def index_of_nearest(numbers, number):
#     if len(numbers) > 0:
#         return numbers.index(min(numbers, key=lambda x: abs(x - number)))
#     else:
#         return -1
#
# print(index_of_nearest([], 17))
# print(index_of_nearest([7, 13, 3, 5, 18], 12))
#
# # Функция index_of_nearest()(ОТ ПРЕПОДАВАТЕЛЯ)
# def index_of_nearest(nums, n):
#     if nums:
#         minimum = min(nums, key=lambda num: abs(num - n))
#         return nums.index(minimum)
#     return -1
#
# # Функция index_of_nearest()(ОТ ПОЛЬЗОВАТЕЛЯ
# def index_of_nearest(numbers, num):
#     return numbers.index(min(numbers, key=lambda x: abs(x - num))) if numbers else -1

# Функция spell()

# def spell(*words):
#     return {el[0].lower(): len(el) for el in sorted(words, key=len)}
#
# print(spell('Математика', 'История', 'химия', 'биология', 'Информатика'))


# Функция spell()(ОТ ПРЕПОДАВАТЕЛЯ)
# def spell(*args):
#     result = {}
#     for word in args:
#         if result.get(word[0].lower(), 0) < len(word):
#             result[word[0].lower()] = len(word)
#     return result
#
# # Функция spell()(ОТ ПОЛЬЗОВАТЕЛЯ)
# def spell(*args):
#     args = sorted(args, key=len)
#     return dict(zip(map(lambda x: x.lower()[0], args), map(len, args)))


# Функция choose_plural()
# def choose_plural(amount, declensions):
#     if amount < 10:
#         if amount % 10 == 1:
#             return f'{amount} {declensions[0]}'
#         elif amount % 10 in (2, 3, 4):
#             return f'{amount} {declensions[1]}'
#         else:
#             return f'{amount} {declensions[2]}'
#
#     elif 9 < amount < 100:
#         if amount % 10 == 1 and amount != 11:
#             return f'{amount} {declensions[0]}'
#         elif amount % 10 in (2, 3, 4) and amount not in (11, 12, 13, 14):
#             return f'{amount} {declensions[1]}'
#         else:
#             return f'{amount} {declensions[2]}'
#
#     elif amount > 99:
#         if amount % 100 % 10 == 1 and amount % 100 != 11:
#             return f'{amount} {declensions[0]}'
#         elif amount % 100 % 10 in (2, 3, 4) and amount % 100 not in (11, 12, 13, 14):
#             return f'{amount} {declensions[1]}'
#         else:
#             return f'{amount} {declensions[2]}'
#
#
#
# # TEST_1:
# print(choose_plural(21, ('пример', 'примера', 'примеров')))


# Функция choose_plural()(ОТ ПРЕПОДАВАТЕЛЯ)
# def choose_plural(amount, variants):
#     variant = 2
#     if amount % 10 == 1 and amount % 100 != 11:
#         variant = 0
#     elif amount % 10 >= 2 and amount % 10 <= 4 and (amount % 100 < 10 or amount % 100 >= 20):
#         variant = 1
#     return '{} {}'.format(amount, variants[variant])

# Функция choose_plural()(ОТ ПОЛЬЗОВАТЕЛЯ)
# def choose_plural(amount: int, declensions: tuple):
#     if str(amount).endswith(('0', '5', '6', '7', '8', '9', '11', '12', '13', '14')):
#         return f'{amount} {declensions[2]}'
#     elif str(amount).endswith('1'):
#         return f'{amount} {declensions[0]}'
#     else:
#         return f'{amount} {declensions[1]}'
#
# # Функция choose_plural()(ОТ ПОЛЬЗОВАТЕЛЯ)(ИСПОЛЬЗОВАНИЕ СЕЛЕКТОРОВ)
# def choose_plural(amount, declensions):
#     selector = {
#         amount % 10 == 1: 0,
#         amount % 10 in [2, 3, 4]: 1,
#         amount % 10 in [0, 5, 6, 7, 8, 9]: 2,
#         amount % 100 in range(11, 21) : 2
#     }
#     return f'{amount} {declensions[selector[True]]}'
#
# # Функция choose_plural()(ОТ ПОЛЬЗОВАТЕЛЯ)
# def choose_plural(number, words):
#     outdict = {0: 2, 1: 0, 2: 1, 3: 1, 4: 1, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2}
#     if number % 100 in range(11, 20):
#         selector = 2
#     else:
#         selector = outdict[number % 10]
#
#     return f'{number} {words[selector]}'


# Функция get_biggest()

# def get_biggest(numbers):
#     # if not numbers:
#     #     return -1
#     nums = [str(el) for el in numbers]
#     m_len = len(max(nums))
#     print(m_len)
    # x = list(sorted(nums, key=max))
    # print(x)
    # number = []
    # while len(nums) != 0:
    #     number.append(max(nums))
    #     del nums[nums.index(max(nums))]
    #
    # return ''.join(number)


# def get_biggest(numbers):
#     if not numbers:
#         return -1
#     # return ''.join(sorted([str(el) for el in numbers], reverse=True))
#     return ''.join(sorted((str(el) for el in numbers), reverse=True))

# print(get_biggest([1, 2, 3]))
# print(get_biggest([]))
# print(get_biggest([61, 228, 9, 3, 11]))
# print(get_biggest([7, 71, 72]))






