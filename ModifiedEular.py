

def f(x, y): v = y - 2 * x * x + 1; return v


def predict(x, y, h):
    y1p = y + h * f(x, y)
    return y1p


def correct(x, y, x1, y1, h):
    e = 0.00001
    y1c = y1

    while (abs(y1c - y1) > e + 1):
        y1 = y1c
        y1c = y + 0.5 * h * (f(x, y) + f(x1, y1))
    return y1c


def printFinalValues(x, xn, y, h):
    while (x < xn):
        x1 = x + h
        y1p = predict(x, y, h)
        y1c = correct(x, y, x1, y1p, h)
        x = x1
        y = y1c
    print("The final value of y at x =", int(x), "is :", y)


if __name__ == '_main_':
    print()
x = 0
y = 0.5
xn = 3
h = 0.2
printFinalValues(x, xn, y, h)
