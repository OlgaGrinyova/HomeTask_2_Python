#Создать список и заполнить его элементами различных типов данных. Реализовать скрипт
#проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
#Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

my_list = [2, 'Olga', True, 2.3, (1, 'Hello'), b'Olik', {'my', 'favorite', 'python'}, None, {'age': 25}, [10, 20, 'text'], (10j + 5j)]
for el in my_list:
    print(type(el))
