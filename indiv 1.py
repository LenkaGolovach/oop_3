#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

class Triangle:
    """
    Класс треугольник с полями-сторонами. Позволяет изменять стороны, вычислять углы и периметр.
    """
    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c

    def read_sides(self):
        # Чтение сторон треугольника с клавиатуры
        self.a = float(input("Введите длину стороны a: "))
        self.b = float(input("Введите длину стороны b: "))
        self.c = float(input("Введите длину стороны c: "))
        if not self.is_triangle_valid():
            print("Треугольник с данными сторонами не существует. Пожалуйста, введите корректные значения.")
            self.read_sides()

    def is_triangle_valid(self):
        # Проверка, может ли существовать треугольник с такими сторонами
        return self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a

    def change_sides(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calculate_angles(self):
        angles = []
        angles.append(math.degrees(math.acos((self.b**2 + self.c**2 - self.a**2) / (2.0 * self.b * self.c))))
        angles.append(math.degrees(math.acos((self.a**2 + self.c**2 - self.b**2) / (2.0 * self.a * self.c))))
        angles.append(math.degrees(math.acos((self.a**2 + self.b**2 - self.c**2) / (2.0 * self.a * self.b))))
        return angles

    def perimeter(self):
        return self.a + self.b + self.c

    def display(self):
        print(f"Стороны треугольника: a={self.a}, b={self.b}, c={self.c}")

class RightAngled(Triangle):
    """
    Производный класс для прямоугольного треугольника.
    """
    def __init__(self):
        # Инициализация прямоугольного треугольника с вводом сторон a и b с клавиатуры
        a = float(input("Введите длину катета a: "))
        b = float(input("Введите длину катета b: "))
        super().__init__(a, b, math.sqrt(a**2 + b**2))

    def area(self):
        return 0.5 * self.a * self.b

    def display(self):
        print(f"Стороны прямоугольного треугольника: a={self.a}, b={self.b}, c={self.c:.2f}, площадь={self.area():.2f}")

if __name__ == '__main__':
    print("Создаем треугольник:")
    triangle = Triangle()
    triangle.read_sides()
    triangle.display()

    angles = triangle.calculate_angles()
    print(f"Углы треугольника: {angles}")

    print(f"Периметр треугольника: {triangle.perimeter()}")

    print("\nСоздаем прямоугольный треугольник:")
    right_angled = RightAngled()
    right_angled.display()
