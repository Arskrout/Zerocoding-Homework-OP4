# -*- coding: utf-8 -*-
# Функция для подсчета суммы всех целых чисел от start до end включительно
def sum_range(start, end):
    # Возвращаем сумму чисел от start до end
    return sum(range(start, end + 1))

# Этап 1: Запрос у пользователя необходимых параметров
print("Enter the start of the range:")  # Введите начало диапазона
start = int(input())

print("Enter the end of the range:")  # Введите конец диапазона
end = int(input())

# Этап 2: Выполнение функции
result = sum_range(start, end)

# Этап 3: Вывод результата функции
print(f"The sum of integers from {start} to {end} is {result}.")  # Сумма чисел от start до end равна result.
