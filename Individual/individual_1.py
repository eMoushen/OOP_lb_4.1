#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class MyPair:

    def __init__(self, first=0.0, second=0.0):
        first = float(first)
        second = float(second)

        self.__first = first
        self.__second = second

    @property
    def first(self):
        return self.__first

    @property
    def second(self):
        return self.__second

    # Прочитать значение
    def read(self):
        self.__first = float(input("Введите значение для первого поля (дробное число): "))
        self.__second = float(input("Введите значение для второго поля (положительное дробное число): "))
        if self.__second <= 0:
            raise ValueError("Значение второго поля должно быть положительным дробным числом")

    # Вывести на экран
    def display(self):
        print(f"First: {self.__first}, Second: {self.__second}")

    # Умножение на произвольное дробное число
    def multiply(self, factor):
        self.__first *= factor
        self.__second *= factor


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