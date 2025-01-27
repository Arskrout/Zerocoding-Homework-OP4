# -*- coding: utf-8 -*-
# Функция для расчета итоговой суммы по вкладу с учетом сложных процентов
def bank(a, years):
    # Процентная ставка (10% годовых)
    rate = 0.10
    # Расчет итоговой суммы по формуле сложных процентов
    final_amount = a * (1 + rate) ** years
    # Возвращаем итоговую сумму
    return final_amount

# Этап 1: Запрос у пользователя необходимых параметров
print("Enter the initial deposit amount (in rubles):")  # Введите сумму первоначального вклада (в рублях)
a = float(input())

print("Enter the deposit period (in years):")  # Введите срок вклада (в годах)
years = int(input())

# Этап 2: Выполнение функции
final_amount = bank(a, years)

# Этап 3: Вывод результата функции
print(f"The total amount after {years} years will be: {final_amount:.2f} rubles.")
# Итоговая сумма после years лет составит final_amount рублей.
