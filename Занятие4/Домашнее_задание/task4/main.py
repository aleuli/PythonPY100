def happy(integer):
    integer_string = [int(d) for d in str(integer)]
    if sum(integer_string[:3]) == sum(integer_string[3:]):
        print("Happy")
    else:
        print(" no happy")



if __name__ == "__main__":

    print(happy(900135))


