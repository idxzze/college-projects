# 1. Дано трехзначное число. Проверить истинность высказывания: «Все цифры данного
# числа различны».

try:
    n = int(input("Введите трехзначное число: "))  # Запрашиваем ввод у пользователя

    if n < 100 or n > 999:
        raise ValueError("Число должно быть трехзначным.")
# Извлекаем сотни, десятки и единицы, проверяем различны ли цифры
    hundreds = n // 100
    tens = (n // 10) % 10
    units = n % 10

    if (hundreds != tens) and (hundreds != units) and (tens != units):
        print("Все цифры различны")
    else:
        print("Цифры не различны")

except ValueError:
    print("Ошибка ввода")
