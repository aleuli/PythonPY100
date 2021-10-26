number = 123456789
list_digit = list(str(number))
for i, str_digit in enumerate(list_digit):
    list_digit[i] = int(str_digit)
print("Список цифр числа N", list_digit)

print("Сумма всех цифр", sum(list_digit))

sum_ = 0
for digit in list_digit:
    if digit % 2 == 0:
        sum_ += digit
print("Сумма всех четных цифр", sum_)

print("Количество цифр в списке", len(list_digit))

print("Минимальная цифра", min(list_digit))

print("Максимальная цифра", max(list_digit))

print("Цифры на нечетных местах",list_digit[::2])
print("Цифры на четных местах",list_digit[1::2])

print("Разность первой и последней цифры", list_digit[0] - list_digit[-1])

min_value_index = 0
min_value = list_digit[min_value_index]
for i,char in enumerate(list_digit):
    if char < min_value:
        min_value = char
        min_value_index = i
print("Минимальная цифра", min_value , "Находится по индексу", min_value_index)

if __name__ == "__main__":
    # Write your solution here
    pass
