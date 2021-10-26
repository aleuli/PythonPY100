def function(a):
    digits_list = [int(d) for d in str(a)]
    if digits_list == digits_list[::-1]:
        print("палиндром")
    else:
        print("Не палиндром")
        return

if __name__ == "__main__":
    a = 2552
    print(function(a))






