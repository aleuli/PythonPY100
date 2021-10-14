A = int(input("Введите число A "))
B = int(input("Введите число B "))
condition1 = A % 2 == 1
condition2 = B % 2 == 1
if condition1 and condition2:
    print("Каждое из числе А и B нечетное")
elif condition1 or condition2:
    print("Какое то из чисел А или В четное ")
else:
    print("Оба числа четные ")

