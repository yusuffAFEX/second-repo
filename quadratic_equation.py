import csv


def quadratic_equation():
    a = int(input('Enter first Number: '))
    b = int(input('Enter second number: '))
    c = int(input('Enter third number: '))
    y = a
    z = c

    if a == -abs(a):
        a = a * -1
    if c == -abs(c):
        c = c * -1

    g = []
    t = []
    m = []
    for i in range(1, a * c):
        g.append(i)
        t.append(i)
    for k in g:
        for j in t:
            if (k + j == b) and (k * j == a*c):
                m.append(k)
            if (k - j == b) and (k * -j == a*c):
                m.append(k)
            if (-k + j == b) and (-k * j == a*c):
                m.append(-k)
            if (-k - j == b) and (-k * -j == a*c):
                m.append(-k)
            # if (k + j == b or -k + j == b or k - j == b or -k - j == b) and (
            #         k * j == a * c or -k * j == a * c or k * -j == a * c or -k * -j == a * c):
            #     m.append(k)
            break
    print(m)


quadratic_equation()

