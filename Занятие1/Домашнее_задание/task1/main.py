cena = int(input("Сколько стоит один ГБ? "))
speed = int(input("ВВедите скорость передачи данных(байт/сек): "))
vremy = int(input("Введите время в минутах потраченное на скачивание игры: "))
b_min = speed * 60 # байты  в минуту
skolko_scachal = b_min * vremy

gb_min = round(skolko_scachal / 1024 / 1024 / 1024, 5)
print("Скачано гигабайт:", gb_min )
if gb_min <= 1:
    print("Бесплатный трафик не израсходован, оплата не требуется")
else:
    print("Вы должны заплатить: ",cena * gb_min, "за скачанные гигабайты.")
