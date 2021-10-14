a = int(input("Введите значение а: "))
condition1 = a % 2 == 0
condition2 = a % 3 == 0
if condition1 or condition2:
    print("Число а кратно 2 или 3 ")
else:
    print("Число не кратно ни 2 ни 3")