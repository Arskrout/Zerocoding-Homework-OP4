# -*- coding: utf-8 -*-
# ������� ��� �������� ����� ���� ����� ����� �� start �� end ������������
def sum_range(start, end):
    # ���������� ����� ����� �� start �� end
    return sum(range(start, end + 1))

# ���� 1: ������ � ������������ ����������� ����������
print("Enter the start of the range:")  # ������� ������ ���������
start = int(input())

print("Enter the end of the range:")  # ������� ����� ���������
end = int(input())

# ���� 2: ���������� �������
result = sum_range(start, end)

# ���� 3: ����� ���������� �������
print(f"The sum of integers from {start} to {end} is {result}.")  # ����� ����� �� start �� end ����� result.
