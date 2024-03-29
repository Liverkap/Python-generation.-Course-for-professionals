
#                   ***********         Модуль datetime
# получение текущих системных даты и времени
# вычисление разницы между датами и другие арифметические операции над ними
# сравнение даты и времени
# форматированный вывод информации о дате и времени


#                           Тип данных date

# Тип данных (класс) date используется для представления данных о дате и включает информацию о годе, месяце и дне.
# Чтобы иметь возможность использовать этот тип данных, необходимо предварительно его импортировать из модуля datetime

# from datetime import date

# my_date = date(1992, 10, 6)
#
# print(my_date)
# print(type(my_date))

# Конструктор типа date сначала принимает год, затем месяц, а уже потом день.
# Мы также можем использовать именованные аргументы, нарушая указанный порядок date(day=6, month=10, year=1992)

# Иногда приходится работать не только с общими сведениями о дате, но и с отдельными ее составляющими,
# такими как год, месяц или день. Получить доступ к ним можно с помощью атрибутов:

# from datetime import date
#
# my_date = date(1992, 10, 6)
#
# print('Год =', my_date.year)
# print('Месяц =', my_date.month)
# print('День =', my_date.day)

# Если необходимо получить информацию о текущей дате на компьютере, на котором выполняется программа, то используется встроенный метод today()

# from datetime import date
#
# creation_date = date.today()
# print(creation_date)

# С помощью встроенного метода weekday() можно определить день недели (нумерация начинается с 0)
# from datetime import date
#
# date1 = date(2022, 10, 15)
# date2 = date(1999, 12, 26)
#
# print(date1.weekday())
# print(date2.weekday())

# Если требуется определить день недели с нумерацией, начиная с 1, то используется метод isoweekday()
# from datetime import date
#
# date1 = date(2022, 10, 15)
# date2 = date(1999, 12, 26)
#
# print(date1.isoweekday())
# print(date2.isoweekday())

# Для получения минимально и максимально возможных дат (в рамках типа данных date) используются атрибуты min и max

# from datetime import date
#
# print(date.min)
# print(date.max)

# Методы fromordinal() и toordinal() позволяют создать дату из номера дня, начиная с 0001-01-01, и наоборот, преобразовать дату в номер дня

# from datetime import date
#
# date1 = date.fromordinal(365)     # дата, соответствуюшая номеру дня 365
# date2 = date(1999, 12, 26)
#
# print(date1)
# print(date2.toordinal())          # номер дня, соответствующий дате 1999-12-26



#                   ***********         Тип данных time     **********

# Тип данных (класс) time используется для представления данных о времени и включает информацию о часах,
# минутах, секундах и микросекундах. Данный тип данных полностью игнорирует информацию о дате
# Микросекунда (мкс) — единица времени, равная одной миллионной доле секунды

# При создании времени (тип данных time) нужно указать часы, минуты, секунды и микросекунды.

# from datetime import time
#
# my_time = time(11, 20, 54, 1234)    # тип time: часы + минуты + секунды + микросекунды
#
# print(my_time)
# print(type(my_time))
#
# Конструктор типа time сначала принимает часы, затем минуты, секунды, а уже потом микросекунды.
# Мы можем использовать именованные аргументы (hour, minute, second, microsecond), нарушая указанный порядок

# Указывая аргументы hour, minute, second, microsecond, не следует забывать про ограничения.
# К примеру, нельзя указать значение hour, большее 23, или значение second, большее 59

# В отличие от дат (тип данных date), чтобы создать объект типа time, необязательно указывать все его атрибуты в конструкторе.
# Недостающие данные о времени автоматически заполняются нулями

# from datetime import time
#
# time1 = time(11, 20, 54, 1234)
# time2 = time(11, 20, 54)
# time3 = time(11, 20)
# time4 = time(11)
# time5 = time()
# time6 = time(minute=23, second=56)
#
# print(time1, time2, time3, time4, time5, sep='\n')
# print(time6)


# Так же, как и при работе с типом данных date, пользуясь типом time, можно получать доступ
# к отдельным значениям созданного времени: часам, минутам, секундам и микросекундам. Получить доступ к ним можно с помощью атрибутов
# from datetime import time
#
# my_time = time(11, 20, 54, 1234)
#
# print('Часы =', my_time.hour)
# print('Минуты =', my_time.minute)
# print('Секунды =', my_time.second)
# print('Микросекунды =', my_time.microsecond)


#               ***********         Сравнение дат и времени     **********
# Дату (тип date) и время (тип time) можно сравнивать с помощью операторов ==, !=, <, >, <= и  >=

# from datetime import date, time
#
# date1 = date(2022, 10, 15)
# date2 = date(1999, 12, 26)
#
# time1 = time(13, 10, 5)
# time2 = time(21, 32, 59)
#
# print(date1 < date2)
# print(time1 < time2)


#               **************      Функции str() и repr()      *****
# На практике часто используются две встроенные функции str() и repr(). С их помощью можно получить строковое представление объекта.
#
# Встроенная функция str() возвращает объект в неформальном (понятном человеку) строковом представлении

# from datetime import date, time
#
# my_date = date(2021, 12, 31)
# my_time = time(11, 20, 54)
#
# print(my_date)
# print(my_time)

# Встроенная функция repr() возвращает объект в формальном (понятном интерпретатору) строковом представлении

# from datetime import date, time
#
# my_date = date(2021, 12, 31)
# my_time = time(11, 20, 54)
#
# print(repr(my_date))
# print(repr(my_time))

# Для встроенных типов данных при печати одиночного значения объекта явно вызывать функцию str() не требуется,
# однако при печати списка таких объектов это требуется

# from datetime import date
#
# dates = [date(2021, 12, 31), date(2019, 10, 6), date(2022, 11, 8)]   # список дат
#
# print(dates)

# Если мы хотим вывести содержимое списка в человеческом виде, то нужно прибегнуть к распаковке,
# в этом случае функция str() будет вызываться для каждого элемента списка за кулисами

# Примечание 1. Оба типа данных date и time являются неизменяемыми. Мы можем создать множества, содержащие объекты
# данных типов (date и time), а также они могут выступать в качестве ключей словаря

# from datetime import date
#
# my_set = {date(2021, 12, 31), date(2019, 3, 19), date(2022, 5, 25)}                # множество
# my_dict = {date(2021, 12, 31): 'Новый год', date(2030, 10, 6): 'День рождения'}    # словарь
#
# print(my_set)
# print(my_dict)

# Примечание 2. Мы можем использовать встроенные функции min(), max(), sorted() и т.д. при работе с типами данных date и time
# from datetime import date
#
# dates = [date(2021, 12, 31), date(2025, 3, 19), date(2017, 5, 25)]
#
# print(min(dates))
# print(max(dates))
# print(sorted(dates))

# Примечание 3. Для создания новой даты на основании уже существующей можно использовать метод replace().
# Он возвращает новую дату с переданными измененными значениями свойств year, month, day
# from datetime import date
#
# date1 = date(1992, 10, 6)
# date2 = date1.replace(year=1995)            # заменяем год
# date3 = date1.replace(month=12, day=17)     # заменяем месяц и число
#
# print(date1)
# print(date2)
# print(date3)
#
# Примечание 4. В качестве ограничений по годам в типе date используются значения MINYEAR=1 и MAXYEAR=9999
#
# Примечание 5. Помните про ограничения на атрибуты (year, month, day, hour, minute, second, microsecond),
# которые используете для создания объектов типов date и time. В случае использования неверного значения возникнет ошибка (исключение) ValueError
#
# Примечание 7. По умолчанию объекты типов date и time выводятся в ISO 8601 формате


# **********
# импортируем тип date из модуля datetime
# from datetime import date

# выводим текущую дату
# print(date.today())


# ***********
# # импортируем тип date из модуля datetime
# from datetime import date
#
# # создаем объект, соответсвующий дате урагана
# hurricane_andrew = date(1992, 8, 24)
#
# # выводим день недели
# print(hurricane_andrew.weekday())

# ********
# # счетчик для нужного количества ураганов
# early_hurricanes = 0
#
# # цикл по датам в которые был ураган
# for hurricane in florida_hurricane_dates:
#     # если месяц урагана меньше чем июнь (порядковый номер 6)
#     if hurricane.month < 6:
#         early_hurricanes += 1
#
# print(early_hurricanes)

# ***********
# from datetime import date
#
# dates = [date(2010, 9, 28), date(2017, 1, 13), date(2009, 12, 25), date(2010, 2, 27), date(2021, 10, 11), date(2020, 3, 13),
#          date(2000, 7, 7), date(1999, 4, 14), date(1789, 11, 19), date(2013, 8, 21), date(1666, 6, 6), date(1968, 5, 26)]

# for el in dates:
#     if el.month < 4:
#         print(f'{el.year}-Q1')
#     elif 3 < el.month < 7:
#         print(f'{el.year}-Q2')
#     elif 6 < el.month < 10:
#         print(f'{el.year}-Q3')
#     else:
#         print(f'{el.year}-Q4')

# *********(ОТ ПРЕПОДАВАТЕЛЯ)
# for d in dates:
#     print(f'{d.year}-Q{(d.month - 1) // 3 + 1}')

# *********(ОТ ПОЛЬЗОВАТЕЛЯ)
# for date in dates:
#     print(f'{date.year}-Q{"111222333444"[date.month-1]}')


# ФУНКЦИЯ GET_MIN_MAX()
# from datetime import date
# def get_min_max(dates):
#     if not dates:
#         return ()
#     sort_dates = sorted(dates)
#     return sort_dates[0], sort_dates[-1]
#
#
# # ФУНКЦИЯ GET_MIN_MAX()(ОТ ПРЕПОДАВАТЕЛЯ)
# def get_min_max(dates):
#     if dates:
#         return min(dates), max(dates)
#     return ()
#
#
# # ФУНКЦИЯ GET_MIN_MAX()(ОТ ПОЛЬЗОВАТЕЛЯ)
# def get_min_max(dates):
#     return tuple(dates) and (min(dates), max(dates))
#
#
# dates = [date(2021, 10, 5), date(1992, 6, 10), date(2012, 2, 23), date(1995, 10, 12)]
#
# print(get_min_max(dates))
# print(get_min_max([]))
