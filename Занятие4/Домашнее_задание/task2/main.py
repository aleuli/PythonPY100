def function(integer:int):
    list_number = [int(d) for d in str(integer)]
    if len(set(list_number)) < len(list_number):
        print("Не все цифры числа уникальны")
    else:
        print("Все цифры числа уникальны")


if __name__ == "__main__":


    print(function(1234561789))

