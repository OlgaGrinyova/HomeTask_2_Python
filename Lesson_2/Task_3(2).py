#Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года
#относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.

#через dict
month = int(input('Введите месяц в виде целого числа от 1 до 12: '))
if month > 12:
    print('Такого месяца не существует, попробуйте еще раз!')

seasons_dict = {'Зима': (12, 1, 2), 'Весна': (3, 4, 5), 'Лето': (6, 7, 8), 'Осень': (9, 10, 11)}
for key in seasons_dict.keys():
    if month in seasons_dict[key]:
        print(key)

#через list
month = int(input('Введите месяц в виде целого числа от 1 до 12: '))
if month > 12:
    print('Такого месяца не существует, введите число от 1 до 12!')

seasons_list = ['Зима', 'Весна', 'Лето', 'Осень']
if month == 12 or month == 1 or month == 2:
    print(seasons_list[0])
elif month == 3 or month == 4 or month == 5:
    print(seasons_list[1])
elif month == 6 or month == 7 or month == 8:
    print(seasons_list[2])
elif month == 9 or month == 10 or month == 11:
    print(seasons_list[3])



