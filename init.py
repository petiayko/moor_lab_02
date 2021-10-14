import re
import copy


# # класс "неравенство системы"
# class Line:
#     def __init__(self):
#         # строка неравенства, прочитанная из файла
#         self.line = ''
#         # число переменных в данной задаче
#         self.variables = -1
#         #
#         self.vector = list()
#         #
#         self.free = int()
#         #
#         self.sign = int()
#
#     # метод проверки корректоности введенных данных
#     def check_validation(self):
#         line = self.line
#         if ('>' in line and '<' not in line) or ('>' not in line and '<' in line):
#             # if line[line.find('=') + 1:].isdigit():
#             pattern = re.compile(r'-?\S*x\d+|-?\S+x?|-?x')
#             line = line[:line.find('<=' * ('<=' in line) + '>=' * ('>=' in line))]
#             if re.match(pattern, line):
#                 return
#         raise Exception('Wrong format of input data')
#
#     # # метод определения знака неравенства
#     # def get_sign(self):
#     #     if not (self.line is None):
#     #         self.check_validation()
#     #         line = self.line
#     #         if ('>=' in line and '<=' not in line) or ('>=' not in line and '<=' in line):
#     #             return 1 - 2 * ('<=' in line)
#     #
#     # # метод определения свободного члена неравенства
#     # def get_free(self):
#     #     if not (self.line is None):
#     #         self.check_validation()
#     #         line = self.line
#     #         return int(line[line.find('<=' * ('<=' in line) + '>=' * ('>=' in line)) + 2:])
#     #
#     # # метод получения списка коэффициентов неравенства
#     # def get_vector(self):
#     #     if not (self.line is None):
#     #         self.check_validation()
#     #         pattern = re.compile(r'-?\d*x\d+|-?\d+x?|-?x')
#     #         line = self.line.replace(',', '')
#     #         line = line.replace('.', '')
#     #         line = line[:line.find('<=' * ('<=' in line) + '>=' * ('>=' in line))]
#     #         line = pattern.findall(line)
#     #         # self.variables = len(line)
#     #         # print(self.variables)
#     #
#     #         vector = [0 for _ in range(self.variables)]
#     #         for term in line:
#     #             if not term[:term.find('x')] or term[:term.find('x')] == '+':
#     #                 vector[int(term[term.find('x') + 1:]) - 1] = 1
#     #             else:
#     #                 if term[:term.find('x')] == '-':
#     #                     vector[int(term[term.find('x') + 1:]) - 1] = -1
#     #                 elif term[:term.find('x')][0] == '0':
#     #                     vector[int(term[term.find('x') + 1:]) - 1] = int(term[:term.find('x')]) / 10
#     #                 else:
#     #                     vector[int(term[term.find('x') + 1:]) - 1] = int(term[:term.find('x')])
#     #
#     #         return vector
#
#     def set_line(self, line):
#         self.line = line
#
#     def set_vector(self, vector):
#         self.vector = vector
#
#     def set_free(self, free):
#         self.free = free
#
#     def set_sign(self, sign):
#         self.free = sign
#
#     def get_vector(self):
#         return self.vector
#
#     def get_free(self):
#         return self.free
#
#     def get_sign(self):
#         return self.sign
#
# # класса "целевая функция"
# class Target:
#     def __init__(self, line=None):
#         # строка целевой функции, прочитанная из файла
#         self.line = line
#         # число переменных в данной задаче
#         self.variables = len(self.get_vector())
#         #
#         self.vector = self.get_vector()
#         #
#         self.free = self.get_free()
#         #
#         self.goal = self.get_goal()
#
#     # метод поверки корректности введенных данных
#     def check_validation(self):
#         if not (self.line is None):
#             line = self.line
#             if '->' in line:
#                 if ('min' in line and 'max' not in line) or ('min' not in line and 'max' in line):
#                     if line.find('m') > line.find('->'):
#                         return
#             raise Exception('Wrong format of input data')
#
#     # метод определения стремления целевой функции (минимум или максимум)
#     def get_goal(self):
#         if not (self.line is None):
#             self.check_validation()
#             line = self.line
#             return 1 - 2 * int('max' in line)
#
#     # метод определения свободного члена целевой фцнкции
#     def get_free(self):
#         if not (self.line is None):
#             self.check_validation()
#             line = self.line
#             pattern = re.compile(r'-?\d*x\d+|-?\d+x?|-?x')
#             line = pattern.findall(line[line.find('=') + 1:line.find('->')])
#             for term in line:
#                 if 'x' not in term:
#                     return int(term)
#             return 0
#
#     # метод получения списка коэффициентов целевой функции
#     def get_vector(self):
#         if not (self.line is None):
#             line = self.line
#             pattern = re.compile(r'-?\d*x\d+|-?\d+x?|-?x')
#             line = pattern.findall(line[line.find('=') + 1:line.find('->')])
#             self.variables = len(line)
#
#             vector = [0 for i in range(self.variables)]
#             for term in line:
#                 if 'x' in term:
#                     if not term[:term.find('x')] or term[:term.find('x')] == '+':
#                         vector[int(term[term.find('x') + 1:]) - 1] = 1
#                     elif term[:term.find('x')] == '-':
#                         vector[int(term[term.find('x') + 1:]) - 1] = -1
#                     else:
#                         vector[int(term[term.find('x') + 1:]) - 1] = int(term[:term.find('x')])
#
#             return vector
#         return []
#
#
# # класс "симплекс-таблица"
# class SimplexTable:
#     def __init__(self, A, c, lines):
#         # A - список объектов класса "неравенство системы" - неравенства системы
#         self.A = A
#         # объект класса "целевая функция" - целевая функция
#         self.c = c
#
#         # симплекс таблица
#         self.table = self.get_simplex_table()
#         # число переменных в данной задаче
#         self.variables = len(self.c.get_vector())
#         #
#         self.lines = lines
#         # список индексов свободных переменных (необходимо для вывода симплекс-таблицы на экран)
#         self.free = [int(i) for i in range(1, self.variables + 1)]
#         # список индексов базисных переменных (необходимо для вывода симплекс-таблицы на экран)
#         self.base = [i + len(self.free) for i in range(1, self.lines + 1) if i + len(self.free) not in self.free]
#         #
#         self.letter = 'x'
#
#     # метод заполнения симплекс-таблицы
#     def get_simplex_table(self):
#         simplex_table = []
#         for i in range(len(self.A)):
#             row = [-self.A[i].get_free() * self.A[i].get_sign()] + [-val * self.A[i].get_sign() for val in
#                                                                     self.A[i].get_vector()]
#             simplex_table.append(row)
#         simplex_table.append([self.c.get_free()] + [-val for val in self.c.get_vector()])
#         return simplex_table
#
#     # метод нахождения разрешающего столбца и строки для поиска оптимального решения
#     def find_pivot_optimise(self):
#         max_abs, support_column = -1, -1
#         for i in range(1, len(self.table[len(self.table) - 1])):
#             if self.table[len(self.table) - 1][i] < 0 and abs(self.table[len(self.table) - 1][i]) > max_abs:
#                 max_abs = abs(self.table[len(self.table) - 1][i])
#                 support_column = i
#         min_div, support_row = 10 ** 8, -1
#         for j in range(len(self.table) - 1):
#             if self.table[j][support_column] != 0:
#                 if abs(self.table[j][0] / self.table[j][support_column]) < min_div:
#                     min_div = abs(self.table[j][0] / self.table[j][support_column])
#                     support_row = j
#         print(f'Pivot column: x{self.free[support_column - 1]}\n'
#               f'Pivot row: x{self.base[support_row]}\n'
#               f'Pivot element: {self.table[support_row][support_column]}\n\n')
#         self.free[support_column - 1], self.base[support_row] = self.base[support_row], self.free[support_column - 1]
#         return support_row, support_column
#
#     # метод нахождения разрешающего столбца и строки для поиска допустимого решения
#     def find_pivot(self):
#         support_row = -1
#         for i in range(len(self.table)):
#             if self.table[i][0] < 0:
#                 support_row = i
#                 break
#         support_column = -1
#         for j in range(1, len(self.table[support_row])):
#             if self.table[support_row][j] < 0:
#                 support_column = j
#                 break
#         print(f'Pivot column: x{self.free[support_column - 1]}\n'
#               f'Pivot row: x{self.base[support_row]}\n'
#               f'Pivot element: {self.table[support_row][support_column]}\n\n')
#         self.free[support_column - 1], self.base[support_row] = self.base[support_row], self.free[support_column - 1]
#         return support_row, support_column
#
#     # метод жорданового исключения
#     def jordan_exception(self, support_row, support_column):
#         pivot = self.table[support_row][support_column]
#         simplex_table_iter = copy.deepcopy(self.table)
#         for i in range(len(simplex_table_iter)):  # rows
#             for j in range(len(simplex_table_iter[0])):  # cols
#                 if i == support_row and j != support_column:
#                     simplex_table_iter[i][j] = round(self.table[i][j] / pivot, 3)
#                 elif i != support_row and j == support_column:
#                     simplex_table_iter[i][j] = round(-self.table[i][j] / pivot, 3)
#                 elif i == support_row and j == support_column:
#                     simplex_table_iter[i][j] = round(1 / pivot, 3)
#                 else:
#                     simplex_table_iter[i][j] = round(self.table[i][j] - (
#                             self.table[support_row][j] * self.table[i][support_column]) / pivot, 3)
#         return simplex_table_iter
#
#     # метод решения задачи (на выходе допустимое оптимальное решение)
#     def solve(self):
#         repetition = 0
#         while True:
#             print(f'Iteration number {repetition}')
#             repetition += 1
#             print(self)
#             if min([i[0] for i in self.table[:len(self.table) - 1]]) < 0:
#                 row, column = self.find_pivot()
#                 self.table = copy.deepcopy(self.jordan_exception(support_column=column, support_row=row))
#                 continue
#             if -self.c.get_goal() * min(self.table[len(self.table) - 1][1:]) < 0:
#                 row, column = self.find_pivot_optimise()
#                 self.table = copy.deepcopy(self.jordan_exception(support_column=column, support_row=row))
#                 continue
#             break
#
#         return [i[0] for i in self.table[:len(self.table[0]) - 1]], self.table[len(self.table) - 1][0]
#
#     # метод печати симплекс-таблицы
#     def __repr__(self):
#         rows = [f'{self.letter}{str(i)}' for i in self.base] + ['F']
#         output = '\t\tC\t\t' + '\t\t'.join([f'{self.letter}{i}' for i in self.free]) + '\n'
#         for i in range(len(self.table)):
#             output += f'{rows[i]}\t\t'
#             for j in range(len(self.table[i])):
#                 output += '%5.3f\t'
#             output = output % tuple(self.table[i])
#             output += '\n'
#         return output


# функция получения симплекс-таблицы для двойственной задачи


# класс "неравенство системы"
class Line:
    def __init__(self, line, variables):
        # строка неравенства, прочитанная из файла
        self.line = line
        # число переменных в данной задаче
        self.variables = variables
        #
        self.vector = list()
        #
        self.sign = 0
        #
        self.free = 0

    # метод проверки корректоности введенных данных
    def check_validation(self):
        line = self.line
        if ('>' in line and '<' not in line) or ('>' not in line and '<' in line):
            # if line[line.find('=') + 1:].isdigit():
            pattern = re.compile(r'-?\S*x\d+|-?\S+x?|-?x')
            line = line[:line.find('<=' * ('<=' in line) + '>=' * ('>=' in line))]
            if re.match(pattern, line):
                return
        raise Exception('Wrong format of input data')

    # метод определения знака неравенства
    def get_sign(self):
        self.check_validation()
        line = self.line
        if ('>=' in line and '<=' not in line) or ('>=' not in line and '<=' in line):
            self.sign = 1 - 2 * ('<=' in line)
            return self.sign

    # метод определения свободного члена неравенства
    def get_free(self):
        self.check_validation()
        line = self.line
        self.free = int(line[line.find('<=' * ('<=' in line) + '>=' * ('>=' in line)) + 2:])
        return self.free

    # метод получения списка коэффициентов неравенства
    def get_vector(self):
        self.check_validation()
        pattern = re.compile(r'-?\d*x\d+|-?\d+x?|-?x')
        line = self.line.replace(',', '')
        line = line.replace('.', '')
        line = line[:line.find('<=' * ('<=' in line) + '>=' * ('>=' in line))]
        line = pattern.findall(line)

        vector = [0 for i in range(self.variables)]
        for term in line:
            if not term[:term.find('x')] or term[:term.find('x')] == '+':
                vector[int(term[term.find('x') + 1:]) - 1] = 1
            else:
                if term[:term.find('x')] == '-':
                    vector[int(term[term.find('x') + 1:]) - 1] = -1
                elif term[:term.find('x')][0] == '0':
                    vector[int(term[term.find('x') + 1:]) - 1] = int(term[:term.find('x')]) / 10
                else:
                    vector[int(term[term.find('x') + 1:]) - 1] = int(term[:term.find('x')])
        self.vector = vector
        return self.vector


# класса "целевая функция"
class Target:
    def __init__(self, line):
        # строка целевой функции, прочитанная из файла
        self.line = line
        # число переменных в данной задаче
        self.variables = len(self.get_vector())
        #
        self.vector = list()
        #
        self.goal = 0
        #
        self.free = 0

    # метод поверки корректности введенных данных
    def check_validation(self):
        line = self.line
        if '->' in line:
            if ('min' in line and 'max' not in line) or ('min' not in line and 'max' in line):
                if line.find('m') > line.find('->'):
                    return
        raise Exception('Wrong format of input data')

    # метод определения стремления целевой функции (минимум или максимум)
    def get_goal(self):
        self.check_validation()
        line = self.line
        self.goal = 1 - 2 * int('max' in line)
        return self.goal

    # метод определения свободного члена целевой фцнкции
    def get_free(self):
        self.check_validation()
        line = self.line
        pattern = re.compile(r'-?\d*x\d+|-?\d+x?|-?x')
        line = pattern.findall(line[line.find('=') + 1:line.find('->')])
        for term in line:
            if 'x' not in term:
                self.free = int(term)
                return self.free
        return 0

    # метод получения списка коэффициентов целевой функции
    def get_vector(self):
        line = self.line
        pattern = re.compile(r'-?\d*x\d+|-?\d+x?|-?x')
        line = pattern.findall(line[line.find('=') + 1:line.find('->')])
        self.variables = len(line)

        vector = [0 for i in range(self.variables)]
        for term in line:
            if 'x' in term:
                if not term[:term.find('x')] or term[:term.find('x')] == '+':
                    vector[int(term[term.find('x') + 1:]) - 1] = 1
                elif term[:term.find('x')] == '-':
                    vector[int(term[term.find('x') + 1:]) - 1] = -1
                else:
                    vector[int(term[term.find('x') + 1:]) - 1] = int(term[:term.find('x')])
        self.vector = vector
        return self.vector


# класс "симплекс-таблица"
class SimplexTable:
    def __init__(self, A, c, lines):
        # A - список объектов класса "неравенство системы" - неравенства системы
        self.A = A
        # объект класса "целевая функция" - целевая функция
        self.c = copy.deepcopy(c)
        # симплекс таблица
        self.table = []
        # self.table = self.get_simplex_table()
        # число переменных в данной задаче
        # self.variables = max([i.variables for i in self.A])
        self.variables = self.c.variables
        #
        self.lines = lines
        # список индексов свободных переменных (необходимо для вывода симплекс-таблицы на экран)
        self.free = [int(i) for i in range(1, self.variables + 1)]
        # список индексов базисных переменных (необходимо для вывода симплекс-таблицы на экран)
        self.base = [i + len(self.free) for i in range(1, self.lines + 1) if i + len(self.free) not in self.free]
        #
        self.letter = 'x'

    # метод заполнения симплекс-таблицы
    def get_simplex_table(self):
        simplex_table = []
        for i in range(len(self.A)):
            row = [-self.A[i].get_free() * self.A[i].get_sign()] + [-val * self.A[i].get_sign() for val in
                                                                    self.A[i].get_vector()]
            simplex_table.append(row)
        simplex_table.append([self.c.get_free()] + [-val for val in self.c.get_vector()])
        self.table = simplex_table
        return self.table

    # метод заполнения симплекс-таблицы
    def get_simplex_table_getter(self):
        simplex_table = []
        for i in range(len(self.A)):
            row = [-self.A[i].free * self.A[i].sign] + [-val * self.A[i].sign for val in self.A[i].vector]
            simplex_table.append(row)
        simplex_table.append([self.c.free] + [-val for val in self.c.vector])
        self.table = simplex_table
        return self.table

    # метод нахождения разрешающего столбца и строки для поиска оптимального решения
    def find_pivot_optimise(self):
        max_abs, support_column = -1, -1
        for i in range(1, len(self.table[len(self.table) - 1])):
            if self.table[len(self.table) - 1][i] < 0 and abs(self.table[len(self.table) - 1][i]) > max_abs:
                max_abs = abs(self.table[len(self.table) - 1][i])
                support_column = i
        min_div, support_row = 10 ** 8, -1
        for j in range(len(self.table) - 1):
            if self.table[j][support_column] != 0:
                if abs(self.table[j][0] / self.table[j][support_column]) < min_div:
                    min_div = abs(self.table[j][0] / self.table[j][support_column])
                    support_row = j
        print(f'Pivot column: x{self.free[support_column - 1]}\n'
              f'Pivot row: x{self.base[support_row]}\n'
              f'Pivot element: {self.table[support_row][support_column]}\n\n')
        self.free[support_column - 1], self.base[support_row] = self.base[support_row], self.free[support_column - 1]
        return support_row, support_column

    # метод нахождения разрешающего столбца и строки для поиска допустимого решения
    def find_pivot(self):
        support_row = -1
        for i in range(len(self.table)):
            if self.table[i][0] < 0:
                support_row = i
                break
        support_column = -1
        for j in range(1, len(self.table[support_row])):
            if self.table[support_row][j] < 0:
                support_column = j
                break
        print(f'Pivot column: x{self.free[support_column - 1]}\n'
              f'Pivot row: x{self.base[support_row]}\n'
              f'Pivot element: {self.table[support_row][support_column]}\n\n')
        self.free[support_column - 1], self.base[support_row] = self.base[support_row], self.free[support_column - 1]
        return support_row, support_column

    # метод жорданового исключения
    def jordan_exception(self, support_row, support_column):
        pivot = self.table[support_row][support_column]
        simplex_table_iter = copy.deepcopy(self.table)
        for i in range(len(simplex_table_iter)):  # rows
            for j in range(len(simplex_table_iter[0])):  # cols
                if i == support_row and j != support_column:
                    simplex_table_iter[i][j] = round(self.table[i][j] / pivot, 3)
                elif i != support_row and j == support_column:
                    simplex_table_iter[i][j] = round(-self.table[i][j] / pivot, 3)
                elif i == support_row and j == support_column:
                    simplex_table_iter[i][j] = round(1 / pivot, 3)
                else:
                    simplex_table_iter[i][j] = round(self.table[i][j] - (
                            self.table[support_row][j] * self.table[i][support_column]) / pivot, 3)
        return simplex_table_iter

    # метод решения задачи (на выходе допустимое оптимальное решение)
    def solve(self):
        repetition = 0
        while True:
            print(f'Iteration number {repetition}')
            repetition += 1
            print(self)
            if min([i[0] for i in self.table[:len(self.table) - 1]]) < 0:
                row, column = self.find_pivot()
                self.table = copy.deepcopy(self.jordan_exception(support_column=column, support_row=row))
                continue
            if -self.c.get_goal() * min(self.table[len(self.table) - 1][1:]) < 0:
                row, column = self.find_pivot_optimise()
                self.table = copy.deepcopy(self.jordan_exception(support_column=column, support_row=row))
                continue
            break

        return [i[0] for i in self.table[:len(self.table[0]) - 1]], self.table[len(self.table) - 1][0]

    # метод печати симплекс-таблицы
    def __repr__(self):
        rows = [f'x{str(i)}' for i in self.base] + ['F']
        output = '\t\tC\t\t' + '\t\t'.join([f'x{i}' for i in self.free]) + '\n'
        for i in range(len(self.table)):
            output += f'{rows[i]}\t\t'
            for j in range(len(self.table[i])):
                output += '%5.3f\t'
            output = output % tuple(self.table[i])
            output += '\n'
        return output


def get_dual(simplex_table):
    simplex_table.get_simplex_table()
    print('Simplex-table for direct task:')
    print(simplex_table)

    A = [i.vector for i in simplex_table.A]
    AT = [[0 for _ in range(len(simplex_table.table) - 1)] for i in range(len(simplex_table.table[0]) - 1)]
    for i in range(len(A)):
        for j in range(len(A[i])):
            AT[j][i] = A[i][j]
    signs = [simplex_table.A[i].get_sign() for i in range(len(simplex_table.A))]
    if len(set(signs)) != 1:
        raise Exception('Wrong data')
    sign = signs[0]
    b = [simplex_table.A[i].get_free() for i in range(len(simplex_table.A))]
    c = simplex_table.c.vector

    A_dual = []
    for i in range(len(AT)):
        line = Line('', variables=len(AT[i]))
        line.vector = AT[i]
        line.sign = sign * (-1)
        line.free = c[i]
        A_dual.append(line)
    c_dual = Target('')
    c_dual.vector = b
    c_dual.variables = len(AT[0])
    # print(simplex_table.c.get_goal())
    c_dual.goal = simplex_table.c.get_goal() * (-1)

    simplex_table_dual = SimplexTable(A_dual, c_dual, len(AT))
    simplex_table_dual.letter = 'y'
    simplex_table_dual.get_simplex_table_getter()
    print(simplex_table_dual)

    # A = []
    # for i in range(simplex_table.variables):
    #     # print(i + 1, simplex_table.A[i].get_vector(), simplex_table.A[i].get_sign())
    #     b.append(simplex_table.A[i].get_free())
    #     line = Line(variables=simplex_table.variables)
    #     line.vector =

    # for i in AT:
    #     print(i)
    # print(b)
    # print(c)

    # b = [i[0] for i in simplex_table.table[:-1]]
    # c = [i for i in simplex_table.table[len(simplex_table.table) - 1][1:]]
    # # print(f'b={b}\nc={c}')
    # A = [[j for j in i[1:]] for i in simplex_table.table[:-1]]
    # AT = [[0 for _ in range(len(simplex_table.table) - 1)] for i in range(len(simplex_table.table[0]) - 1)]
    # for i in range(len(A)):
    #     for j in range(len(A[i])):
    #         AT[j][i] = A[i][j]

    # new_simplex_table = [[c[i]] + [-j for j in AT[i]] for i in range(len(c))]
    # new_simplex_table.append([0] + [-i for i in b])
    # dual = SimplexTable(simplex_table.A, simplex_table.c, len(AT))
    # dual.variables = len(AT[0])
    #
    # dual.table = new_simplex_table
    # dual.free = [i for i in range(1, dual.variables + 1)]
    # dual.letter = 'y'

    # print('Simplex-table for dual task:')
    # print(dual)
