pi = 3.14592653589793238462643383279502
def f(n):  # Calculating Factorial
    if n == 1 or n == 0:
        return 1
    else:
        return n * f(n - 1)

def deg(x): # Converting Degrees to Radians
    rad = x * pi/180
    return rad

def sin(x):  # Using Taylor Series
    x = deg(x)
    k = 0
    sinx = 0
    while x >= pi:
        x -= pi
    if pi > x > pi / 2:
        x = pi - x
    while k < 15:
        sinx += (-1)**k * x**(2*k + 1) / f(2*k + 1)
        k += 1
    return sinx
