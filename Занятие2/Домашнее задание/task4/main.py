if __name__ == "__main__":
    # Write your solution here
    list_ = list(range(11))
    a = list_[0]
    b = max(list_)
    print("минимальный элемент", a)
    print("максимальный элемент", b)
    tmp = a
    a = b
    b = tmp
    print("новый максимальный элемент", a)
    print("новый минимальный элемент", b)
