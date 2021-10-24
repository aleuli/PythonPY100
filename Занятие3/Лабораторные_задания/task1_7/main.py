def student(a,b,s):
    m = 0
    while 0 < s :
        s += a
        b = b + (b * 0.05)
        s -= b
        m += 1
        print("Я прожил", m,"месяцев")
    return m
if __name__ == "__main__":
    print(student(1000,1500,30000))