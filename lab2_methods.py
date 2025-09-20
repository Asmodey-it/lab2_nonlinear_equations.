import math

# Функція рівняння
def f(x):
    return x**4 + 2*x**3 + 2*x**2 + 6*x - 3

# Відокремлення коренів
def find_segments(start, end, step):
    segments = []
    a = start
    prev_val = f(a)
    x = start + step
    while x <= end:
        curr_val = f(x)
        if prev_val * curr_val < 0:
            segments.append((a, x))
        a = x
        prev_val = curr_val
        x += step
    return segments

# Метод половинного ділення
def bisection(a, b, eps):
    while abs(b - a) > eps:
        c = (a + b) / 2.0
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2.0

# Метод хорд
def chord(a, b, eps):
    x0 = a
    xi = b
    xi1 = xi - (xi - x0) * f(xi) / (f(xi) - f(x0))

    while abs(xi1 - xi) > eps:
        xi = xi1
        xi1 = xi - (xi - x0) * f(xi) / (f(xi) - f(x0))
    return xi1

if __name__ == "__main__":
    eps = 0.0001
    print("Рівняння: x^4 + 2x^3 + 2x^2 + 6x - 3 = 0")
    print("Точність:", eps, "\n")

    segments = find_segments(-10, 10, 1)

    for a, b in segments:
        print(f"Відрізок [{a}; {b}]")
        print("Метод половинного ділення:", bisection(a, b, eps))
        print("Метод хорд:", chord(a, b, eps), "\n")
