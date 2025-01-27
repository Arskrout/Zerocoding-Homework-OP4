# -*- coding: utf-8 -*-
# ������� ��� ������� �������� ����� �� ������ � ������ ������� ���������
def bank(a, years):
    # ���������� ������ (10% �������)
    rate = 0.10
    # ������ �������� ����� �� ������� ������� ���������
    final_amount = a * (1 + rate) ** years
    # ���������� �������� �����
    return final_amount

# ���� 1: ������ � ������������ ����������� ����������
print("Enter the initial deposit amount (in rubles):")  # ������� ����� ��������������� ������ (� ������)
a = float(input())

print("Enter the deposit period (in years):")  # ������� ���� ������ (� �����)
years = int(input())

# ���� 2: ���������� �������
final_amount = bank(a, years)

# ���� 3: ����� ���������� �������
print(f"The total amount after {years} years will be: {final_amount:.2f} rubles.")
# �������� ����� ����� years ��� �������� final_amount ������.
