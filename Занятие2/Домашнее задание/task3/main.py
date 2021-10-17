# TODO
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))
rezultat1 = a < 45 and 45 <= b and 45 <= c
rezultat2 = 45 <= a and 45 > b and 45 <= c
rezultat3 = 45 <=a and 45 <= b and 45 > c
if rezultat1 or rezultat2 or rezultat3:
    print("Условие истинно")
else:
    print("Условие ложно")

