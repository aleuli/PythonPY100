# TODO
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
summa_kvadratov = (a ** 2) +(b ** 2)
kvadrat_summi = (a + b) ** 2
if summa_kvadratov < kvadrat_summi:
    print("Сумма квадратов меньше квадрата суммы")
elif summa_kvadratov > kvadrat_summi:
    print("Сумма квадратов больше квадрата суммы")
elif summa_kvadratov == kvadrat_summi:
    print("Сумма квадратов равна квадрату суммы")