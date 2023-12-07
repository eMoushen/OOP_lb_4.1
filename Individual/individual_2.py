#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math


class Vector:

    def __init__(self, x=0, y=0, z=0):
        x = float(x)
        y = float(y)
        z = float(z)

        self._x = x
        self._y = y
        self._z = z

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def z(self):
        return self._z

    # Прочитать координаты с клавиатуры
    def read(self, prompt=None):
        line = input() if prompt is None else input(prompt)
        parts = list(map(float, line.split()))

        if len(parts) != 3 or parts[2] == 0:
            raise ValueError()

        self._x, self._y, self._z = parts

    # Вывести координаты на экран
    def display(self):
        print(f"Координаты - {self._x}, {self._y}, {self._z}")

    # Сложение векторов
    def add(self, rhs):
        if isinstance(rhs, Vector):
            return Vector(self.x + rhs.x, self.y + rhs.y, self.z + rhs.z)
        else:
            raise ValueError()

    # Вычитание векторов
    def sub(self, rhs):
        if isinstance(rhs, Vector):
            return Vector(self.x - rhs.x, self.y - rhs.y, self.z - rhs.z)
        else:
            raise ValueError()

    # Скалярное произведение векторов
    def dot(self, rhs):
        if isinstance(rhs, Vector):
            return Vector(self.x * rhs.x, self.y * rhs.y, self.z * rhs.z)
        else:
            raise ValueError()

    # Умножение вектора на скаляр
    def scalar_multiply(self, scalar):
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    # Сравнение векторов
    def equals(self, rhs):
        if isinstance(rhs, Vector):
            return "Векторы совпадают" if (self.x == rhs.x) and (self.y == rhs.y) and (
                        self.z == rhs.z) else "Векторы не совпадают"
        else:
            raise ValueError()

    # Вычисление длины вектора
    def length(self):
        return math.sqrt(pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2))

    # Сравнение длины векторов
    def compare_length(self, rhs):
        if isinstance(rhs, Vector):
            length_self = self.length()
            length_rhs = rhs.length()

            if length_self > length_rhs:
                return "Длина первого вектора больше длины второго вектора"
            elif length_self < length_rhs:
                return "Длина первого вектора меньше длины второго вектора"
            else:
                return "Длины векторов равны"
        else:
            raise ValueError()


if __name__ == "__main__":
    v1 = Vector(1, 2, 3)
    v1.display()

    v2 = Vector()
    v2.read("Введите координаты: ")
    v2.display()

    v3 = v2.add(v1)
    v3.display()

    v4 = v2.sub(v1)
    v4.display()

    v5 = v2.dot(v1)
    v5.display()

    scalar = 2
    v6 = v1.scalar_multiply(scalar)
    v6.display()

    print(v1.equals(v2))
    print(v1.length())
    print(v2.compare_length(v1))