# -*- coding: utf-8 -*-
# Функция для вычисления периметра, площади и диагонали квадрата
def square(side):
    # Периметр квадрата
    perimeter = 4 * side
    # Площадь квадрата
    area = side ** 2
    # Диагональ квадрата
    diagonal = (2 ** 0.5) * side
    # Возвращаем результаты в виде кортежа
    return perimeter, area, diagonal

# Этап 1: Запрос у пользователя необходимого параметра
print("Enter the side length of the square:")  # Введите длину стороны квадрата
side = float(input())

# Этап 2: Выполнение функции
perimeter, area, diagonal = square(side)

# Этап 3: Вывод результата функции
print(f"The perimeter, area, and diagonal of the square are: {perimeter:.2f}, {area:.2f}, {diagonal:.2f}.")
# Периметр, площадь и диагональ квадрата равны: perimeter, area, diagonal.
