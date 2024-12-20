# Дано вещественное число X (|X|<1) и целое число N (>0). Найти значение выражения
# X - X2/2 + X3/3 - ... + (-1) N-1XN/N. Полученное число является приближенным
# значением функции ln в точке 1 + X.

# Пользователь вводит значения X и N
X = float(input("Введите вещественное число X (|X| < 1): "))
N = int(input("Введите целое число N (>0): "))

# Программа проверяет что введенные данные соответствуют |X| < 1 и N > 0. Если условие не выполнено выводит ошибку.
if abs(X) >= 1 or N <= 0:
    print("Ошибка: Убедитесь что |X| < 1 и N > 0")
else:
    result = 0.0

# Используем цикл for чтобы пройти от 1 до N, затем вычисляя каждый член ряда и добавляя его к переменной result.
    for n in range(1, N + 1):
        term = ((-1 ) ** (n - 1)) * (X ** n) / n 
        result += term

# Выводим результат решенный программмой.
    print(f"Приближенное значение ln(1 + {X}) равно {result}.") 