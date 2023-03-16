"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов
класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
"""


class Matrix:
    num_of_row = 0

    def __init__(self, input_list):
        self.row = []
        for el in range(len(input_list)):
            self.row.append(input_list[self.num_of_row])
            self.num_of_row += 1

    def __str__(self):
        result = ''
        for i in range(self.num_of_row):
            for j in self.row[i]:
                result = result + str(j) + ' '
            result.strip()
            result = result + '\n'
        return result

    def __add__(self, other):
        result_list = []
        if self.num_of_row == other.num_of_row and len(self.row) == len(other.row):
            for i in range(self.num_of_row):
                new_row = []
                for j in range(len(self.row[i])):
                    new_row.append(int(self.row[i][j]) + int(other.row[i][j]))
                result_list.append(new_row)
            return Matrix(result_list)
        else:
            return "This matrix can't be stacked"


matrix_two = Matrix([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

matrix_one = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix_one)
print(matrix_two)
sum_matrix = matrix_one + matrix_two
print(f"Sum: \n{sum_matrix}")
