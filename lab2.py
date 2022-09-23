import sys
import math

class SquareRoots:

    def __init__(self):
        '''
        Конструктор класса
        '''
        # Объявление коэффициентов
        self.coef_A = 0.0
        self.coef_B = 0.0
        self.coef_C = 0.0
        # Количество корней
        self.num_roots = 0
        # Список корней
        self.roots_list = []

    def get_coef(self, index, prompt):
        '''
        Читаем коэффициент из командной строки или вводим с клавиатуры
        Args:
            index (int): Номер параметра в командной строке
            prompt (str): Приглашение для ввода коэффицента
        Returns:
            float: Коэффициент квадратного уравнения
        '''
        try:
            # Пробуем прочитать коэффициент из командной строки
            coef_str = sys.argv[index]
        except:
            # Вводим с клавиатуры
            print(prompt)
            coef_str = input()
        # Заставляем пользователя совершить повторный ввод, если у него не получилось
        coef = 0.0
        try_again = True
        while try_again:
            try:
                # Пробуем перевести строку в действительное число
                coef = float(coef_str)
                try_again = False
            except:
                # Вводим с клавиатуры
                print(prompt)
                coef_str = input()
        return coef

    def get_coefs(self):
        '''
        Чтение трех коэффициентов
        '''
        self.coef_A = self.get_coef(1, 'Введите коэффициент А:')
        self.coef_B = self.get_coef(2, 'Введите коэффициент B:')
        self.coef_C = self.get_coef(3, 'Введите коэффициент C:')

    def bigD_to_roots(self, bigD):
        if bigD == 0.0:
            root = math.sqrt(bigD)
            self.num_roots += 1
            self.roots_list.append(root)
        elif bigD > 0.0:
            root = math.sqrt(bigD)
            self.num_roots += 2
            self.roots_list.append(root)
            self.roots_list.append(-root)

    def calculate_roots(self):
        '''
        Вычисление корней квадратного уравнения
        '''
        a = self.coef_A
        b = self.coef_B
        c = self.coef_C
        # Вычисление дискриминанта и корней
        D = b*b - 4*a*c
        if D == 0.0:
            bigD = -b / (2.0*a)
            self.bigD_to_roots(bigD)
        elif D > 0.0:
            sqD = math.sqrt(D)
            bigD = (-b + sqD) / (2.0*a)
            self.bigD_to_roots(bigD)
            bigD = (-b - sqD) / (2.0*a)
            self.bigD_to_roots(bigD)

    def print_roots(self):
        # Проверка отсутствия ошибок при вычислении корней
        if self.num_roots != len(self.roots_list):
            print(('Ошибка. Уравнение содержит {} действительных корней, ' +\
                'но было вычислено {} корней.').format(self.num_roots, len(self.roots_list)))
        else:
            texts = ['Нет корней', 'Один корень: ', 'Два корня: ', 'Три корня: ', 'Четыре корня: ']
            print(texts[self.num_roots], end = '')
            for i in self.roots_list:
                print(i, end = ' ')
            print('')


def main():
    '''
    Основная функция
    '''
    # Создание объекта класса
    r = SquareRoots()
    # Последовательный вызов необходимых методов
    r.get_coefs()
    r.calculate_roots()
    r.print_roots()

# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()

# Пример запуска
# lab1.py 1 0 -4
