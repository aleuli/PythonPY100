if __name__ == "__main__":
    # Write your solution here
    list_ = [1,2,3,4,5,6,7,8,9,10]
    a = list_[0]
    b = max(list_)
    print("минимальный элемент", a)
    print("максимальный элемент", b)
    tmp = a
    a = b
    b = tmp
    print("новый максимальный элемент", a)
    print("новый минимальный элемент", b)
