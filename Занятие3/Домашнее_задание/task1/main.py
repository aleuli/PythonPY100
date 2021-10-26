def poisk():
    diapazon = list(range(3,13))
    while True:
        input_number = int(input("Введите число"))
        input_number = input_number in diapazon
        if input_number < 0:
            break
        print(diapazon)



if __name__ == "__main__":
    # Write your solution here
    pass
print(poisk())