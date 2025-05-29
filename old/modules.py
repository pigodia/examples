# '''
# import tests

# print(tests.a)
# print (tests.b)
# print (tests.c)'''

# '''
# from tests import A, B, C

# print(A)
# print(B)
# print(C)'''
# '''from . import tests as ts 

# print(ts.A)
# print(ts.B)
# print(ts.C)
# '''
# '''from os import dsa as  ds

# print(ds.welcome("Nastya"))'''
# list=[1,2,3,4]
# from random import (randint, choice, shuffle,
#                 sample, random, choices,
#                 randrange)
#print(choice([1,2,3,4]))#выберает эллемент из списка
#shuffle(list)#рандомно перемешивает лист
#print(list)

# print(sample(list,3))#3- эт сколько надо выбрать
# print(choices(list, k = 3))#3- эт сколько надо выбрать это тоже самое что и choice 
# print(random())
# print(randrange(0, 10, 2))


# from datetime import datetime, timedelta, date, time

# print(datetime.now()) #текущая дата и время 
# print(datetime.today()) # дата и время (типо now)




# dt = dt = datetime.now().strftime("Дата %d.%m.%Y время %H:%M:%S")
# print(dt)

# dt = datetime.now()
# print("Год:", dt.year)
# print("Месяц:", dt.month)
# print("Год:", dt.day)
# print("Год:", dt.hour)
# print("Год:", dt.minute)
# print("Год:", dt.second)
# print("Микросек"б dt.microsecond)
# print("День недели:", dt.weekday())
# print("День недели число", dt.isoweekday())


# dt = datetime(2023, 10, 1, 12, 30, 45))
# dt += timedelta(days=5, hours=3, minuts=30))#отнимаем время или прибовляем в зависимости от знака
# print(dt)

# print(date.today().year)
# print(date.today().month)
# print(date.today().day)

# print(time(12, 30, 45))#создание обьекта тайм
# print(time(12, 30, 45).hour)#вывод часа
# print(time(12, 30, 45).minute)
# print(time(12, 30, 45).second)
# print(time(12, 30, 45).microsecond)


# from os import (name, getcwd, 
#                 chdir, listdir, rmdir, mkdir,
#                 remove, rename, system)

# print("Имя операционной системы", name)
# print("Текущая рабочая дирестория", getcwd())
# chdir("..") #изменяет тякущею рабочию дерикторию на родительскую
# print("Список файлов и папок в текущей дериктоии", listdir())
# mkdir("new_folder")#создание новой папки
# rmdir("new_folder") #удаление папки (должна быть пустой)
# remove("file.txt") #удаление файла 
# rename("file.txt", "new_file.txt")#переменоувывает 
# system('ls') #выполнение команды в терминали mac/linux)

# from sys import (version, platform)
# print(version)#версия
# print(platform)#операционная система


# ### 📁 Импорт модулей и организация кода

# 1. Создай модуль `math_utils.py` с переменными PI = 3.14, E = 2.71 и функцией circle_area(r). Импортируй его в основном файле и выведи результаты.
# 2. Импортируй модуль `random` двумя способами:

#    * Полностью (import random)
#    * Частично (from random import choice, randint)
#    * Используй оба способа и объясни, в чём разница при вызове функций.


from random import randint, random, choice 
PI = 3.14
E = 2.71
