def function(list_):
    dlinna = len(list_)
    summa = sum(list_)
    chislo = summa / dlinna
    return ([i for i in list_ if i > chislo])


if __name__ == "__main__":
    list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(function(list_))