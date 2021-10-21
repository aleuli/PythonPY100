def palindrom(s):
    if s == s[::-1]:
        print("Это палиндром")
    else:
        print("Не палиндром")
    return s
if __name__ == "__main__":
    print(palindrom("AKAA"))
