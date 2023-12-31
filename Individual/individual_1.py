#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class MyPair:

    def __init__(self, value1=0.0, value2=0.0):
        value1 = float(value1)
        value2 = float(value2)

        self.__value1 = value1
        self.__value2 = value2

    @property
    def value1(self):
        return self.__value1

    @property
    def value2(self):
        return self.__value2

    # Прочитать значение
    def read(self):
        self.__value1 = float(input("Введите значение для первого поля (дробное число): "))
        self.__value2 = float(input("Введите значение для второго поля (положительное дробное число): "))
        if self.__value2 <= 0:
            raise ValueError("Значение второго поля должно быть положительным дробным числом")

    # Вывести на экран
    def display(self):
        print(f"Value1: {self.__value1}, Value2: {self.__value2}")

    # Умножение на произвольное дробное число
    def multiply(self, factor):
        self.__value1 *= factor
        self.__value2 *= factor


def make_pair(first, second):
    """
    Функция создания экземпляра класса MyPair, принимая значения полей как аргументы
    """
    return MyPair(first, second)


if __name__ == '__main__':
    pair = MyPair()
    pair.read()
    pair.display()

    factor = float(input("Введите множитель для умножения: "))
    pair.multiply(factor)
    print("Результат умножения:")
    pair.display()