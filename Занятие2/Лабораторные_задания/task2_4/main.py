if __name__ == "__main__":
    # stroka = "Hello , World"
    # count_space = len(stroka)
    #
    # for i in range(count_space):
    #     print((i + 5) * " " + stroka[i])
    #
    #
    # for i in :
    #     print(i * " ")# а по возможности дать переменным осмысленные названия и использовать их
    # # TODO Распечатать строку лесенкой
    stroka = "Hello,world"
    for offset, char in enumerate(stroka,start=5):
        print(offset * " " + char)
