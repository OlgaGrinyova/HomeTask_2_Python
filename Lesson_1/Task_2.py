time = int(input('Введите время в секундах: '))

hours = time // 3600 # введенное время делим на 3600 сек и берем целое число
minutes = (time - hours * 3600) // 60 # от введенного времени отнимаем часы * 3600 и делим на количество секунд в минуте
seconds = time - (hours * 3600 + minutes * 60)
print(f'time: {hours:02}:{minutes:02}:{seconds:02}')
