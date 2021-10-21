def main():
    pervoe_chislo = 0
    vtoroe_chislo = 0
    skolko_chisel = 0
    while ((pervoe_chislo ** 2) + (vtoroe_chislo ** 2)) < 500:
        pervoe_chislo += 1
        vtoroe_chislo += 1
        skolko_chisel = pervoe_chislo + vtoroe_chislo
    return skolko_chisel,pervoe_chislo,vtoroe_chislo




if __name__ == "__main__":
    # Write your solution here
    pass
print(main())