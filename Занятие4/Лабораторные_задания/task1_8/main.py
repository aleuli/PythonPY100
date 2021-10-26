def function(list_):
    return ([i ** 3 if 0 < i else 0
             for i in list_])

if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    print(function(list_))
