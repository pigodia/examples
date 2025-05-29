# ### 📁 Импорт модулей и организация кода

# 1. Создай модуль `math_utils.py` с переменными PI = 3.14, E = 2.71 и функцией circle_area(r). Импортируй его в основном файле и выведи результаты.
# 2. Импортируй модуль `random` двумя способами:

#    * Полностью (import random)
#    * Частично (from random import choice, randint)
#    * Используй оба способа и объясни, в чём разница при вызове функций.


# def circle_area(r):
#     PI = 3.14
#     S=PI*r*r
#     return S


from random import *
# E = 2.71
# print(circle_area(randint(1,100)))



# ### 🎲 Работа с модулем `random`
# 3. Создай список из 10 случайных чисел от 1 до 100.
# 4. Перемешай список и выбери 3 элемента без повторений.
# 5. Смоделируй бросок 2 кубиков 100 раз. Подсчитай, сколько раз выпала сумма 7.
# 6. Выведи 5 случайных паролей длиной 8 символов из букв и цифр (используй sample и string.ascii_letters + string.digits).

# list = []
# for i in range(10):
#     list.append(randint(1,100))
# shuffle(list)
# for i in range(3):
#     a=(choice(list)) 
#     print(a)
#     list.remove(a)


# list1 = []
# list2 = []
# k = 0
# for i in range(10):
#     list1.append(randint(1,10))
#     list2.append(randint(1,10))
# for i in range(100):
#     a = choice(list1)
#     b = choice(list2)
#     if a + b == 7:
#         k += 1

# print(k)

# import string 
# chars = string.ascii_letters + string.digits
# password = []
# for i in range(5):
#     for j in range(8):
#         password.append(random.sample(chars, 1)[0])
#     print(password.split())
#     password.clear()

# ### 🕒 Работа с `datetime`, `date`, `time`, `timedelta`

# 7. Выведи текущую дату и время в формате: `ДД.ММ.ГГГГ ЧЧ:ММ:СС`.
# 8. Создай дату своего дня рождения. Определи, сколько дней прошло с этого дня.
# 9. Сколько дней осталось до Нового года?
# 10. Создай объект `datetime` на 1 октября 2023 года 12:00 и прибавь к нему 3 дня и 5 часов.

from datetime import *

# dt = datetime.now().strftime("Дата %d.%m.%Y время %H:%M:%S")
# print(dt)

# dt = datetime(2009, 10, 1, 12, 30, 45))
# dt += timedelta(days=5, hours=3, minuts=30))#отнимаем время или прибовляем в зависимости от знака
# print(dt)


# dt = datetime(2023, 10, 1, 12, 30, 45)
# print(dt)

# print(date.today().year)
# print(date.today().month)
# print(date.today().day)



# ### 📂 Работа с `os`

# 11. Создай папку `test_dir`, внутри неё файл `hello.txt`. Напиши в файл "Hello, World!" и затем прочитай содержимое.
# 12. Переименуй папку `test_dir` в `demo_dir` и затем удали её.
# 13. Выведи список всех файлов и папок в текущей директории.
# 14. Определи, в какой ОС ты работаешь и какая у тебя текущая рабочая директория.

from os import*
mkdir("new_folder")#создание новой папки








