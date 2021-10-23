def remove_whitespace(str_):
    list_words = str_.split( )
    separator = " ".join(list_words)
    return separator# TODO с помощью методов строки join и split очистить строку от лишних пробелов


if __name__ == "__main__":
    str_with_space = "    123.    test   print test11    "  # исходная строка
    print(remove_whitespace(str_with_space))
