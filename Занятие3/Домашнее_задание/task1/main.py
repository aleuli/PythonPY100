def function( ):
    while True:
        chislo = int(input("введи число: "))
        if not chislo in range(3,14):
            print("такого числа в последовательности нет")
            break
    return chislo


if __name__ == "__main__":
    print(function( ))



