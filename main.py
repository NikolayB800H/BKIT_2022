# Используется для сортировки
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
 
def main():
    # Соединение данных один-ко-многим 
    one_to_many = [(comp.name, comp.cost, clas.name) 
        for clas in classes 
        for comp in computers 
        if comp.clas_id == clas.id]
    
    # Соединение данных многие-ко-многим
    many_to_many_tmp = [(clas.name, compclas.clas_id, compclas.comp_id) 
        for clas in classes 
        for compclas in computers_classes 
        if clas.id == compclas.clas_id]
    
    many_to_many = [(comp.name, comp.cost, clas_name) 
        for clas_name, clas_id, comp_id in many_to_many_tmp
        for comp in computers if comp.id == comp_id]
 
    print('Задание В1')
    res_11 = list(filter(lambda x: x[0].find('А') == 0, one_to_many))
    print(res_11)
    
    print('\nЗадание В2')
    res_12_unsorted = []
    # Перебираем все дисплейные классы
    for clas in classes:
        # Список компьютеров дисплейного класса
        clas_comps = list(filter(lambda i: i[2] == clas.name, one_to_many))
        # Если дисплейный класс не пустой        
        if len(clas_comps) > 0:
            # Стоимости компьютеров дисплейного класса
            clas_costs = list(map(lambda x: x[1], clas_comps))
            # Минимальная стоимость среди компьютеров дисплейного класса
            clas_costs_min = min(clas_costs)
            res_12_unsorted.append((clas.name, clas_costs_min))
 
    # Сортировка по минимальной стоимости
    res_12 = sorted(res_12_unsorted, key = itemgetter(1))
    print(res_12)
 
    print('\nЗадание В3')
    # Сортировка по дисплейному классу
    res_13 = sorted(many_to_many, key = itemgetter(2))
    print(res_13)
 
if __name__ == '__main__':
    main()
