from os import system
system("cls")
from math import*

# print(abs(-10))
# print(abs(1.20))
# print(divmod(10,3))

# print(max([1,2,3,4,5]))
# print(max(1,2,3,4,5))
# print(min([1,2,3,4,5]))
# print(min(1,2,3,4,5))

# print(pow(2, 3))

# print(round(1.9234234))#округляет

# print(sum([1, 2, 3, 4]))
# print(sum([1,2]))

# #all возвращает тру если все элементы истины
# print(all([True,True,True]))

# #any возвращае тру если хотя бы один элемент истинный
# print(any([False, True, False]))

# #all возвращает фолс если все элементы ложны
# print(all([False, False, False]))


# #Показывает тип данных

# print(type(123))
# print(type("abc"))
# print(type([]))


# nums = [1, 2, 3, 4, 5]
# for i, num in enumerate(nums, start=5):
#     print(i, num)
# #


# names = ["John", "Jane"]
# ages = [20, 21]

# zipped = list(zip(names, ages))
# print(zipped)
# #[('John', 20), ('Jane', 21)]



# nums = [1, 2, 3, 4, 5]

# rev = list(reversed(nums))#[5, 4, 3, 2, 1]
# print(rev)


# print(sorted(nums))#сортирует
# print(sorted(nums, reverse=True))


# it = iter([10, 20, 30])
# print(next(it))#10
# print(next(it))#20
# print(next(it,'end'))#30
# print(next(it,'end'))#end (тк элементов больше нет )


# ---

# def square(x):
#     return x**2

# def is_even(x):
#     return x % 2 == 0

# nums = [1, 2, 3, 4, 5]

# print(list(map(str, nums)))
# print(list(map(square, nums)))


# print(list(filter(is_even, nums)))


#1
# list = list(map(int, input().split()))
# list2 = []
# for i in range(len(list)):
#     list2.append(bool(list[i]>0))

# print(all(list2))

#2

# list = list(map(int, input().split()))
# list2 = []
# for i in range(len(list)):
#     list2.append(bool(list[i]<0))

# print(any(list2))


#3

# list1 = str(input())
# list2 = str(input())

# l1 = len(list1)
# l2 = len(list2)
# if  l1 > l2:
#     print("первая строка длиннее," , l1)
# else:
#     print("вторая строка длиннее," , l2)


#4 
# def is_even(x):
#     return x % 2 == 0
# list1 = list(map(int, input().split()))
# print(sum(list(filter(is_even, list1))))

#5

# list = ["sdf", "", "sdfsdf", "sdf"]
# list1 = []
# for i in range(len(list)):
#     list1.append(bool(list[i] != ""))

# print(all(list1))
    

#6 

# def is_even(x):
#     return x % 2 == 0
# list1 = list(map(int, input().split()))
# print(any(list(filter(is_even, list1))))


#7
# def polozh(x):
#     return x > 0
# list1 = list(map(int, input().split()))
# print(sum(list(filter(polozh, list1))))

#8
# list1 = list(map(int, input().split()))
# list2 = list(map(int, input().split()))

# l1 = len(list1)
# l2 = len(list2)
# if  l1 > l2:
#     print("первый список длиннее," , l1)
# elif l1 < l2:
#     print("второй список длиннее," , l2) 

# else:
#     print(list(zip(list1, list2)))

#9
string1 = str(input())
string2 = str(input())
list = []
print(len(string1))
print(len(string2))
list.append(string1)
list.append(string2)

print(sorted(list))


