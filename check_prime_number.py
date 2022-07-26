def prime_number(num: int):
    u = []
    for i in range(1, num+1):
        t = num%i
        u.append(t)
    if u.count(0) == 2:
        return True
    return False

print(prime_number(1))


# def check_prime_number(num: int):
#     flag = [1, num]
#
#     for i in range(1, num+1):
#         if num%i == 0 and i not in flag:
#             return False
#     return True
#
# print(check_prime_number(1))

