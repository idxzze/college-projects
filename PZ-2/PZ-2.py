
#Дано трехзначное число. Вывести число, полученное при перестановке цифр десятков
#и единиц исходного числа (например, 123 перейдет в 132)

try:
    # Ввод трехзначного числа
    number = int(input("Введите трехзначное число: "))
    
    # Проверка, что число трехзначное
    if number < 100 or number > 999:
        raise ValueError("Число должно быть трехзначным!")

    # Извлечение цифр
    hundreds = number // 100
    tens = (number // 10) % 10
    units = number % 10

    # Перестановка цифр десятков и единиц
    new_number = hundreds * 100 + units * 10 + tens

    # Вывод результата
    print("Число после перестановки:", new_number)

except ValueError:
    print("Ошибка")
