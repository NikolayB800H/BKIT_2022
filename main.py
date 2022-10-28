# Используется для сортировки
from operator import itemgetter
 
class Driver:
    """Водитель"""
    def __init__(self, id, fio, sal, park_id):
        self.id = id
        self.fio = fio
        self.sal = sal
        self.park_id = park_id
 
class Park:
    """Автопарк"""
    def __init__(self, id, name):
        self.id = id
        self.name = name
 
class DriverPark:
    """
    'Водители автопарка' для реализации 
    связи многие-ко-многим
    """
    def __init__(self, park_id, driver_id):
        self.park_id = park_id
        self.driver_id = driver_id
 
# Автопарки
parks = [
    Park(1, 'Автопарк "Такси"'),
    Park(2, 'Автопарк "Драйв"'),
    Park(3, 'Автопарк "Бумер"'),
 
    Park(11, 'Автопарк "Такси" (другой)'),
    Park(22, 'Автопарк "Драйв" (другой)'),
    Park(33, 'Автопарк "Бумер" (другой)'),
]
 
# Водители
drivers = [
    Driver(1, 'Артамонов', 25000, 1),
    Driver(2, 'Петров', 35000, 2),
    Driver(3, 'Иваненко', 45000, 3),
    Driver(4, 'Иванов', 35000, 3),
    Driver(5, 'Иванин', 25000, 3),
]
 
drivers_parks = [
    DriverPark(1, 1),
    DriverPark(2, 2),
    DriverPark(3, 3),
    DriverPark(3, 4),
    DriverPark(3, 5),
 
    DriverPark(11, 1),
    DriverPark(22, 2),
    DriverPark(33, 3),
    DriverPark(33, 4),
    DriverPark(33, 5),
]
 
def main():
    """Основная функция"""
 
    # Соединение данных один-ко-многим 
    one_to_many = [(d.fio, d.sal, p.name) 
        for p in parks 
        for d in drivers 
        if d.park_id == p.id]
    
    # Соединение данных многие-ко-многим
    many_to_many_tmp = [(p.name, dp.park_id, dp.driver_id) 
        for p in parks 
        for dp in drivers_parks 
        if p.id == dp.park_id]
    
    many_to_many = [(d.fio, d.sal, park_name) 
        for park_name, park_id, driver_id in many_to_many_tmp
        for d in drivers if d.id == driver_id]
 
    print('Задание 1')
    res_11 = list(filter(lambda x: x[0].find('А') == 0, one_to_many))
    print(res_11)
    
    print('\nЗадание 2')
    res_12_unsorted = []
    # Перебираем все автопарки
    for p in parks:
        # Список водителей автопарка
        p_drivers = list(filter(lambda i: i[2] == p.name, one_to_many))
        # Если отдел не пустой        
        if len(p_drivers) > 0:
            # Зарплаты водителей автопарка
            p_sals = list(map(lambda x: x[1], p_drivers))
            # Минимальная зарплата водителей автопарка
            p_sals_min = min(p_sals)
            res_12_unsorted.append((p.name, p_sals_min))
 
    # Сортировка по минимальной зарплате
    res_12 = sorted(res_12_unsorted, key = itemgetter(1))
    print(res_12)
 
    print('\nЗадание 3')
    # Сортировка по Автопарку
    res_13 = sorted(many_to_many, key = itemgetter(2))
    print(res_13)
 
if __name__ == '__main__':
    main()
