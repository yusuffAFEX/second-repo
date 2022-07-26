def perfect_number(number: int):
    div = []

    for i in range(1, number):
        if number % i == 0:
            div.append(i)
    return sum(div) == number

print(perfect_number(28))