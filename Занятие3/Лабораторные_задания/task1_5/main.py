def poisk():
    sum_ = 0
    while True:
        input_number = int(input("ввдите число: "))
        if input_number == 0:
            print("Введен 0 , стоп")
            break
        sum_ += input_number
        print("Ответ", sum_)


if __name__ == "__main__":
    # Write your solution here
    pass
print(poisk())