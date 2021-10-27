def function(str):
    str_lower = str.lower()
    dict_ = {}
    for symbol in str_lower:
        if not symbol.isalpha():
            continue
        if not symbol in dict_:
            chet = 0
            for newsymbol in str_lower:
                if symbol == newsymbol:
                    chet += 1
        else:
            continue

        dict_[symbol] = chet

    return dict_


def calculate_procent(dic):
    dict_ = dic
    schet = 0
    for symbol in dict_:
        if dict_[symbol] > schet:
            schet = dict_[symbol]
    for symbol in dict_:
        res = dict_[symbol] * 100 / schet
        dict_[symbol] = res
    return dict_












if __name__ == "__main__":
    main_str = """
        Данное предложение будет разбиваться на отдельные слова. 
        В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
        Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
    """

# print(function(main_str))
print(calculate_procent(function(main_str)))

