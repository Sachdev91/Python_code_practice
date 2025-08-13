import math

PI = math.pi

def circle(r):
    c = 2*PI*r
    a = 2*PI*r**2

    return round(c), round(a)


print(circle(4))