def function(integer:int):
    integers_string = [int(d) for d in str(integer)]
    print(integers_string)
    join_num = "".join([str(d) for d in integers_string])
    print(join_num)
    if join_num == join_num[::-1]:
        print("Все цифры одинаковые")
    else:
        print("не одинаковые")



if __name__ == "__main__":

    print(function(4444444444444444444444444444))

