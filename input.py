from init import Target, Line, SimplexTable


# функция чтения данных из файла.
# все строки преобразует в объекты соответствующих классов, собирает их в списки и возвращает
def get_lines(file):
    A = []
    c = None
    lines = [line.replace('\n', '') for line in file]
    for line in lines:
        if 'F=' not in line:
            row = Line(line=line, variables=len(lines) - 1)
            A.append(row)
        else:
            c = Target(line=line, variables=len(lines) - 1)

    return A, c


# функиця решения задачи.
# получает данные из файла и при помощи класса "симплекс-таблица" получает и печатает ответ
def solve(path):
    A, c = get_lines(open(path, 'r'))
    simplex_table = SimplexTable(A, c)
    X, F_val = simplex_table.solve()
    ind = 0
    print('The answer is:')
    for i in simplex_table.base:
        print(f'x{i} = {X[ind]}')
        ind += 1
    print(f'F = {F_val}')


def dual(path):
    A, c = get_lines(open(path, 'r'))
    simplex_table = SimplexTable(A, c)
    simplex_table.get_dual()
