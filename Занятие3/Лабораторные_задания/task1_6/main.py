def student(a, b):
    mounth = 10
    trata = 0
    while 0 < mounth:
        mounth -= 1
        b = b + (b * 0.03)

        trata = trata + (b - a)
    return trata
if __name__ == "__main__":

    print("Студенту дополнительно нужно: ",int(student(10000,11000)),"чтобы прожить 10 месяцев")

