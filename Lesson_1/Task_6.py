#Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
#Каждый день спортсмен увеличивал результат на 10 % относительнопредыдущего.
#Требуется определить номер дня, на который результат спортсмена составит не менее b километров.
#Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

first_result = float(input('Введите результат пробежки в первый день в км: '))
desired_result = float(input('Введите желаемый результат в км: '))
day = 1
while first_result < desired_result:
    first_result = first_result * 1.1
    day = day + 1
print('Цель будет достигнута на', day, 'день')


