#Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются
#элементы с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний
#сохранить на своем месте. Для заполнения списка элементов необходимо использовать функцию input().

number_of_elements = int(input('Введите количество элементов: '))
my_list = [input('Введите элемент: ') for el in range(0, number_of_elements)]
print(my_list)

for el in range(0, number_of_elements - 1, 2):
    my_list[el], my_list[el + 1] = my_list[el + 1], my_list[el]
print(my_list)