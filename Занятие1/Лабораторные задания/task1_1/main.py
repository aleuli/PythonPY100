DAYS_OF_YEAR = 365  # количество дней в году

start_year = int(input("ВВедите год рождения?"))  # TODO запросить у пользователя год рождения
current_year = int(input("Какой сейчас год?"))  # TODO запросить у пользователя текущий год

Col_old_days = (current_year - start_year) * 365
print(Col_old_days)# TODO посчитать и распечатать количество прожитых дней
