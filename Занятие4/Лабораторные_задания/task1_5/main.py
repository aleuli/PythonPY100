# def function(list_):
#     chet = 0
#     nechet = 0
#     return ([i for i in list_ if i % 2 == 0 chet += 1 else nechet +=1])

if __name__ == "__main__":
    list_ = [4, -1, 10, -1, 3, -3, -6, 8, 6, 9]
    chet = 0
    nechet = 0
    for i in list_:
        if i % 2 == 0:
            chet += 1
        else:
            nechet += 1
    if chet > nechet:
            print("Четных больше")
    elif chet == nechet:
        print("Одинаково")
    else:
        print("Нечетных больше")
