import pytest
from modules.DataBase import *

# Дисплейный классы
classes = [
    DispClass(1, 'Класс информатики'),
    DispClass(2, 'Класс генной инженерии'),
    DispClass(3, 'Класс 3Д моделирования'),

    DispClass(11, 'Класс информатики (другой)'),
    DispClass(22, 'Класс генной инженерии (другой)'),
    DispClass(33, 'Класс 3Д моделирования (другой)'),
]

# Компьютеры
computers = [
    Computer(1, 'Делл_АУМ01', 125000, 1),
    Computer(2, 'Эпл__АУМ02', 135000, 2),
    Computer(3, 'Асус_АУМ03', 145000, 3),
    Computer(4, 'Делл_АУМ04', 135000, 3),
    Computer(5, 'Асус_АУМ05', 125000, 3),
]

# Данные о связи многие-ко-многим
computers_classes = [
    ComputerDispClass(1, 1),
    ComputerDispClass(2, 2),
    ComputerDispClass(3, 3),
    ComputerDispClass(3, 4),
    ComputerDispClass(3, 5),
 
    ComputerDispClass(11, 1),
    ComputerDispClass(22, 2),
    ComputerDispClass(33, 3),
    ComputerDispClass(33, 4),
    ComputerDispClass(33, 5),
]

def test_task_b1():
    db = DataBase(classes, computers, computers_classes)
    assert db.task_b1() == [
        ('Асус_АУМ03', 145000, 'Класс 3Д моделирования'),
        ('Асус_АУМ05', 125000, 'Класс 3Д моделирования')
    ]

def test_task_b2():
    db = DataBase(classes, computers, computers_classes)
    assert db.task_b2() == [
        ('Класс информатики', 125000),
        ('Класс 3Д моделирования', 125000),
        ('Класс генной инженерии', 135000)
    ]

def test_task_b3():
    db = DataBase(classes, computers, computers_classes)
    assert db.task_b3() == [
        ('Асус_АУМ03', 145000, 'Класс 3Д моделирования'),
        ('Асус_АУМ03', 145000, 'Класс 3Д моделирования (другой)'),
        ('Асус_АУМ05', 125000, 'Класс 3Д моделирования'),
        ('Асус_АУМ05', 125000, 'Класс 3Д моделирования (другой)'),
        ('Делл_АУМ01', 125000, 'Класс информатики'),
        ('Делл_АУМ01', 125000, 'Класс информатики (другой)'),
        ('Делл_АУМ04', 135000, 'Класс 3Д моделирования'),
        ('Делл_АУМ04', 135000, 'Класс 3Д моделирования (другой)'),
        ('Эпл__АУМ02', 135000, 'Класс генной инженерии'),
        ('Эпл__АУМ02', 135000, 'Класс генной инженерии (другой)')
    ]
