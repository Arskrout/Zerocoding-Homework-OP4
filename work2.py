# -*- coding: utf-8 -*-
# ������� ��� ���������� ���������, ������� � ��������� ��������
def square(side):
    # �������� ��������
    perimeter = 4 * side
    # ������� ��������
    area = side ** 2
    # ��������� ��������
    diagonal = (2 ** 0.5) * side
    # ���������� ���������� � ���� �������
    return perimeter, area, diagonal

# ���� 1: ������ � ������������ ������������ ���������
print("Enter the side length of the square:")  # ������� ����� ������� ��������
side = float(input())

# ���� 2: ���������� �������
perimeter, area, diagonal = square(side)

# ���� 3: ����� ���������� �������
print(f"The perimeter, area, and diagonal of the square are: {perimeter:.2f}, {area:.2f}, {diagonal:.2f}.")
# ��������, ������� � ��������� �������� �����: perimeter, area, diagonal.
