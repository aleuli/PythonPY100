if __name__ == "__main__":
    # Write your solution here
    pass
a = 334
digits_list = [int(d) for d in str(a)]
if sum(digits_list) in list(range(10,100)):
    print(sum(digits_list),"Сумма его цифр - двузначна")
else:
    print("Нет")





