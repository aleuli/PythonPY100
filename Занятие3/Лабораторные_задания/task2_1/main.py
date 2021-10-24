def task(str1, str2, k):
    if str1[:k + 1] == str2[:k + 1]:
        print("Да")
    else:
        print("Нет")# TODO проверка совпадения строк
    return

if __name__ == "__main__":
    print(task("Hello", "Herry", 0))
