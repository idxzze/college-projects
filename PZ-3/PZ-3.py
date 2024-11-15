# 1. Дано трехзначное число. Проверить истинность высказывания: «Все цифры данного
# числа различны».

try:
    n = int(input("Введите трехзначное число: "))  # Запрашиваем ввод у пользователя

    if n < 100 or n > 999:
        raise ValueError("Число должно быть трехзначным.")

    hundreds = n // 100        # Сотни
    tens = (n // 10) % 10      # Десятки
    units = n % 10             # Единицы

    if (hundreds != tens) and (hundreds != units) and (tens != units):
        print("Все цифры различны")
    else:
        print("Цифры не различны")

except ValueError:
    print("Ошибка ввода")
except Exception:
    print("Произошла ошибка")