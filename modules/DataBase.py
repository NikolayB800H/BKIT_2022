from operator import itemgetter

class Computer:
    """Компьютер"""
    def __init__(self, id, name, cost, clas_id):
        self.id = id
        self.name = name
        self.cost = cost
        self.clas_id = clas_id

class DispClass:
    """Дисплейный класс"""
    def __init__(self, id, name):
        self.id = id
        self.name = name

class ComputerDispClass:
    """
    'Компьютеры дисплейного класса' для реализации 
    связи многие-ко-многим
    """
    def __init__(self, clas_id, comp_id):
        self.clas_id = clas_id
        self.comp_id = comp_id

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

class DataBase:
    """
    БД с исходными и промежуточными данными
    """
    def __init__(self, classes, computers, computers_classes):
        self.classes = classes
        self.computers = computers
        self.computers_classes = computers_classes
        self.one_to_many = [(comp.name, comp.cost, clas.name) 
            for clas in classes 
            for comp in computers 
            if comp.clas_id == clas.id]
        many_to_many_tmp = [(clas.name, compclas.clas_id, compclas.comp_id) 
            for clas in classes 
            for compclas in computers_classes 
            if clas.id == compclas.clas_id]
        self.many_to_many = [(comp.name, comp.cost, clas_name) 
            for clas_name, clas_id, comp_id in many_to_many_tmp
            for comp in computers if comp.id == comp_id]

    def task_b1(self):
        res_11 = list(filter(lambda x: x[0].find('А') == 0, self.one_to_many))
        return res_11

    def task_b2(self):
        res_12_unsorted = []
        for clas in classes:
            clas_comps = list(filter(lambda i: i[2] == clas.name, self.one_to_many))
            if len(clas_comps) > 0:
                clas_costs = list(map(lambda x: x[1], clas_comps))
                clas_costs_min = min(clas_costs)
                res_12_unsorted.append((clas.name, clas_costs_min))
        res_12 = sorted(res_12_unsorted, key = itemgetter(1))
        return res_12

    def task_b3(self):
        return sorted(self.many_to_many, key = itemgetter(0))
