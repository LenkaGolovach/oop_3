#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
import math

class Root(ABC):
    """
    Абстрактный базовый класс для корня.
    """

    @abstractmethod
    def calculate(self):
        """
        Абстрактный метод для вычисления корней.
        """

    @abstractmethod
    def display(self):
        """
        Абстрактный метод для вывода результатов на экран.
        """

class Linear(Root):
    """
    Класс для линейного уравнения.
    """
    def __init__(self):
        self.a = 0
        self.b = 0
        self.root = None

    def read_data(self):
        self.a = float(input("Введите коэффициент a линейного уравнения (a*x + b = 0): "))
        self.b = float(input("Введите коэффициент b линейного уравнения (a*x + b = 0): "))

    def calculate(self):
        if self.a == 0:
            if self.b == 0:
                self.root = "Бесконечное количество решений"
            else:
                self.root = "Нет решений"
        else:
            self.root = -self.b / self.a

    def display(self):
        print(f"Корень линейного уравнения: {self.root}")

class Square(Root):
    """
    Класс для квадратного уравнения.
    """
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
        self.roots = None

    def read_data(self):
        self.a = float(input("Введите коэффициент a квадратного уравнения (a*x^2 + b*x + c = 0): "))
        self.b = float(input("Введите коэффициент b квадратного уравнения (a*x^2 + b*x + c = 0): "))
        self.c = float(input("Введите коэффициент c квадратного уравнения (a*x^2 + b*x + c = 0): "))

    def calculate(self):
        discriminant = self.b**2 - 4*self.a*self.c
        if discriminant > 0:
            x1 = (-self.b + math.sqrt(discriminant)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(discriminant)) / (2 * self.a)
            self.roots = (x1, x2)
        elif discriminant == 0:
            x = -self.b / (2 * self.a)
            self.roots = (x,)
        else:
            self.roots = "Корней нет"

    def display(self):
        print(f"Корни квадратного уравнения: {self.roots}")

def demonstrate_virtual_call(root_object):
    """
    Функция для демонстрации виртуального вызова методов.
    """
    root_object.read_data()
    root_object.calculate()
    root_object.display()

if __name__ == "__main__":
    print("Работа с линейным уравнением:")
    linear_equation = Linear()
    demonstrate_virtual_call(linear_equation)

    print("\nРабота с квадратным уравнением:")
    square_equation = Square()
    demonstrate_virtual_call(square_equation)
