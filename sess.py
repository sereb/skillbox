print("Введите первую точку")
x1 = float(input('X: '))
y1 = float(input('Y: '))

print("\nВведите вторую точку")
x2 = float(input('X: '))
y2 = float(input('Y: '))

x_diff = x1 - x2
y_diff = y1 - y2
k = 0
if x_diff != 0:
    k = y_diff / x_diff
    b = y2 - k * x2
    print("\nУравнение прямой, проходящей через эти точки:")
    print("y = ", k, " * x + ", b)
else:
    print("\nУравнение прямой, проходящей через эти точки:")
    print("x =", x1)




