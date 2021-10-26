def function (list_):
    dlinna = len(list_)
    summa = sum(list_)
    sr_arifm = summa / dlinna
    return ([i - sr_arifm for i in list_])


if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    print(function(list_))














#
#
# def function(list):
#     dlinna = len(list)
#     summa = sum(list)
#     chislo = summa / dlinna
#     return ([i for i in list_ if i > chislo])
#
#
# if __name__ == "__main__":
#     list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     print(function(list_))