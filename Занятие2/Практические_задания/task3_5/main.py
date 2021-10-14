wind = int(input("Ввелите скорость ветра: "))
if wind in range(1,5):
    print("Слабый Ветер")
elif wind in range(5,11):
    print("Умеренный ветер")
elif wind in range(11, 19):
    print("Ветер сильный")
elif wind > 19:
    print("Ураганный ветер")
else:
    ...
# TODO напишите с помощью if-elif-else условие проверки скорости ветра
