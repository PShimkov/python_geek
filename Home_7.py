from abc import ABC, abstractmethod



##Задача 1#
class Matrix:

    def __init__(self, input_matrix):
       self.matrix = input_matrix

    def __str__(self):
        return '\n'.join([' '.join([str(elem) for elem in line]) for line in self.matrix])

    def __add__(self, other):

        answer = ''
        if len(self.matrix) == len(other.matrix):
            for line_1, line_2 in zip(self.matrix, other.matrix):
                if len(line_1) != len(line_2):
                    return 'Problems with shape'
                summed_line = [x + y for x, y in zip(line_1, line_2)]
                answer += ' '.join([str(i) for i in summed_line]) + '\n'
        else:
            return 'Problems with shape'
        return answer


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6], [7, 8]])
matrix_2 = Matrix([[2, 3], [4, 5], [6, 7], [10, 20]])

print(matrix_1, matrix_2)
print(matrix_1 + matrix_2)
#Задача 2
class Cloth(ABC):

    def __init__(self, V, H):
        self.V = V
        self.H = H


    @abstractmethod
    def sqare_cloth(self):
        pass

class Coat(Cloth):

    @property
    def sqare_cloth(self):
        return self.V/6.5 + 0.5

class Suit(Cloth):

    @property
    def sqare_cloth(self):
        return 2 * self.H + 0.3

coat_1 = Coat(10, 10)
suit_1 = Suit(10, 10)
print(coat_1.sqare_cloth)
print(suit_1.sqare_cloth)

#Задача 3

class Cell:

    def __init__(self, numbers):
        self.numbers = int(numbers)

    def __str__(self):
        return self.numbers

    def __add__(self, other):
        return str(self.numbers + other.numbers)

    def __sub__(self, other):
        return self.numbers - other.numbers if (self.numbers - other.numbers) > 0 else print('Minus!')

    def __mul__(self, other):
        return str(self.numbers * other.numbers)

    def __truediv__(self, other):
        return round(self.numbers // other.numbers)

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.numbers // rows)]) + '\n' + '*' * (self.numbers % rows)


cell_1 = Cell(150)
cell_2 = Cell(40)
print(cell_1 + cell_2)
print(cell_2.make_order(8))
