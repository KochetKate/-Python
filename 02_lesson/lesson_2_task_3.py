from math import ceil


def square(side):
    return ceil(side * side)


sq_area = float(input("Сторона квадрата = "))
print(f"Площадь квадрата = {square(sq_area)}")
