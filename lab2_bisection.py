import math

# Функція рівняння
def f(x):
    return x**4 + 2*x**3 + 2*x**2 + 6*x - 3

# Метод половинного ділення
def bisection(a, b, eps):
    step = 0
    while abs(b - a) > eps:
        c = (a + b) / 2.0
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        step += 1
    return (a + b) / 2.0

if __name__ == "__main__":
    eps = 0.0001

    # Вибираємо відрізки з коренями
    a1, b1 = -2, -1
    a2, b2 = 0, 1

    print("Метод половинного ділення")
    print("Рівняння: x^4 + 2x^3 + 2x^2 + 6x - 3 = 0")
    print("Точність:", eps, "\n")

    root1 = bisection(a1, b1, eps)
    print(f"Корінь на відрізку [{a1}; {b1}] ≈ {root1}")

    root2 = bisection(a2, b2, eps)
    print(f"Корінь на відрізку [{a2}; {b2}] ≈ {root2}")
