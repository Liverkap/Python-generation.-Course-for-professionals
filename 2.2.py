









# СХОЖИЕ БУКВЫ

# en = 'AaBCcEeHKMOoPpTXxy'
# ru = 'АаВСсЕеНКМОоРрТХху'
#
# new_list = []
#
# for _ in range(3):
#     x = input()
#     if x in en:
#         new_list.append(True)
#     if x in ru:
#         new_list.append(False)
#
# if all(new_list):
#     print('en')
# elif any(new_list):
#     print('mix')
# else:
#     print('ru')


# СХОЖИЕ БУКВЫ(ОТ ПРЕПОДАВАТЕЛЯ)
# langs = ['ru', 'mix', 'mix', 'en']
# eng = 'AaBCcEeHKMOoPpTXxy'
# ind = sum(input() in eng for _ in range(3))
# print(langs[ind])


# СХОЖИЕ БУКВЫ(ОТ ПОЛЬЗОВАТЕЛЯ)
# letters = [input() for _ in range(3)]
# if all(map(lambda x: x in 'АаВСсЕеНКМОоРрТХху', letters)):
#     print('ru')
# elif all(map(lambda x: x in 'AaBCcEeHKMOoPpTXxy', letters)):
#     print('en')
# else:
#     print('mix')


# СХОЖИЕ БУКВЫ(ОТ ПОЛЬЗОВАТЕЛЯ)
# eng = set("AaBCcEeHKMOoPpTXxy")
# rus = set("АаВСсЕеНКМОоРрТХху")
#
# let = set(input()+input()+input())
#
# print(('mix', 'en', 'ru')[let.issubset(eng) - let.issubset(rus)])


# СХОЖИЕ БУКВЫ(ОТ ПОЛЬЗОВАТЕЛЯ)
# a = set([input() for _ in range(3)])
# if a.issubset(set("AaBCcEeHKMOoPpTXxy")):
#     print('en')
# elif a.issubset(set("АаВСсЕеНКМОоРрТХху")):
#     print('ru')
# else:
#     print('mix')


# СХОЖИЕ БУКВЫ(ОТ ПОЛЬЗОВАТЕЛЯ)
# def check(symbols, *args):
#     count = 0
#     for letter in args:
#         if letter in symbols:
#             count += 1
#     return count
#
#
# def result(*args):
#     count_en = check("AaBCcEeHKMOoPpTXxy", *args)
#     count_ru = check("АаВСсЕеНКМОоРрТХху", *args)
#     if count_ru and count_en:
#         return "mix"
#     if count_ru:
#         return "ru"
#     if count_en:
#         return "en"
#
#
# letters = [input() for _ in range(3)]
# print(result(*letters))


# ПЕРЕВОРАТОР




# БОЛЕЕ ОДНОГО

# numbers = [int(num) for num in input().split()]
#
# new_list = []
# for el in numbers:
#     if numbers.count(el) > 1 and el not in new_list:
#         new_list.append(el)
#
# print(*sorted(new_list))

# БОЛЕЕ ОДНОГО (ЕЩЕ ВАРИАНТ)
# numbers = [int(num) for num in input().split()]
# nums = list(filter(lambda x: numbers.count(x) > 1, set(numbers)))
# print(*sorted(nums))
#
# # БОЛЕЕ ОДНОГО (ОТ ПРЕПОДАВАТЕЛЯ)
# nums = [int(i) for i in input().split()]
# print(*sorted(filter(lambda i: nums.count(i) > 1, set(nums))))
#
# # БОЛЕЕ ОДНОГО (ОТ ПОЛЬЗОВАТЕЛЯ)
# d = {}
# for _ in map(int, input().split()):
#     d[_] = d.get(_, 0) + 1
# print(*sorted(list(filter(lambda x: d[x] > 1, d.keys()))))

# # БОЛЕЕ ОДНОГО (ОТ ПОЛЬЗОВАТЕЛЯ)
# nums = list(map(int, input().split()))
# print(*set(i for i in nums if nums.count(i) > 1))

# # БОЛЕЕ ОДНОГО (ОТ ПОЛЬЗОВАТЕЛЯ)(ЧЕРЕЗ СЛОВАРЬ)
# nums = {}
# for num in map(int, input().split()):
#     nums[num] = nums.get(num, 0) + 1
#
# print(*sorted([k for k, v in nums.items() if v > 1]))




