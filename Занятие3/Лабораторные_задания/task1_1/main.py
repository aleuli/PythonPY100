def main():
    pervoe_chislo = 0
    vtoroe_chislo = 0
    skolko_chisel = 0
    schetchik = 0
    while ((pervoe_chislo ** 2) + (vtoroe_chislo ** 2)) in range(0,500):
        pervoe_chislo += 1
        print("Первое число", pervoe_chislo)
        vtoroe_chislo += 1
        print("второе число", vtoroe_chislo)
        skolko_chisel = (pervoe_chislo ** 2) + (vtoroe_chislo ** 2)
        print("Сумма квадратов двух чисел", skolko_chisel)
        schetchik += 1
        print("Таких чисел", schetchik)
    return "Колличество чисел сумма квадратов которых не превышает 500 ", schetchik - 1, "чисел"




if __name__ == "__main__":
    # Write your solution here
    pass
print(main())