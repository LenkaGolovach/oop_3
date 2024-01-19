#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

class Triad:
    """
    Класс "Триада", содержит в себе 3 целочисленных значения
    """
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def add_number(self, number: int):
        """
        Операция сложения с числом
        """
        self.a = self.a + number
        self.b = self.b + number
        self.c = self.c + number

    def mul_number(self, number: int):
        """
        Операция умножения на число
        """
        self.a = self.a * number
        self.b = self.b * number
        self.c = self.c * number

    def __eq__(self, other):
        """
        Операция сравнения с другой триадой
        """
        return self.a == other.a and self.b == other.b and self.c == other.c

    def display(self):
        """
        Печать на консоль
        """
        print(f"Triad(a: {self.a}, b: {self.b}, c: {self.c})")


class Vector3D(Triad):
    """
    Класс "Вектор", наследующийся от класса "Триада"
    """
    def add_vector(self, other):
        """
        Определим метод сложения векторов
        """
        self.a = self.a + other.a
        self.b = self.b + other.b
        self.c = self.c + other.c

    def mul_vector(self, other):
        """
        Определим метод умножения векторов
        """
        self.a = self.a * other.a
        self.b = self.b * other.b
        self.c = self.c * other.c

    def display(self):
        print(f"Vector3D(a: {self.a}, b: {self.b}, c: {self.c})")


if __name__ == '__main__':
    # Создаем две триады
    triad1 = Triad(10, 20, 30)
    triad2 = Triad(40, 80, 50)

    # К первой триаде добавим число 10
    triad1.add_number(10)
    triad1.display()

    # Умножим первую триаду на 2
    triad1.mul_number(2)
    triad1.display()

    # Сравним первую и вторую триаду
    print(triad1 == triad2)

    # Создадим два вектора
    vector1 = Vector3D(5, 7, 9)
    vector2 = Vector3D(2, 4, 6)

    # Добавим к первому вектору второй
    vector1.add_vector(vector2)
    vector1.display()

    # Умножим первый вектор на второй
    vector1.mul_vector(vector2)
    vector1.display()
