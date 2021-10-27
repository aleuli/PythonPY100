def func(a):
    list_simple_numbers = []
    for current_number in range(a + 1):
        m = 0
        for n in range(1,current_number + 1):
            if current_number % n == 0:
                m += 1
        if m == 2:
            list_simple_numbers.append(current_number)
    return list_simple_numbers

print(func(1))



# def func(number, list_prime_numbers):
#     prime_factors = []
#     while number != 1:
#         for prime_numbers in list_prime_numbers:
#             while number % prime_numbers == 0:
#                 prime_factors.append(prime_numbers)
#                 number //= prime_numbers
#     return prime_factors
#
# print(func())
#
#
#





if __name__ == "__main__":
    # Write your solution here
    pass
