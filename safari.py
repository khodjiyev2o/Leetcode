from random import choice, randint


class Safari:
    animals = ('D', 'W', 'T', 'L')

    def __init__(self) -> None:
        self.field = [[choice(self.animals) for _ in range(10)] for _ in range(10)]
        self.used_cells = []
        self.steps = ((-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1), (1, -1))

    def get_random_cell(self) -> tuple[int]:
        return (randint(1, 10), randint(1, 10))

    def get_adjacent_cells(self, cell: tuple[int]) -> list[tuple[int, int]]:
        a, b = cell
        adjacent = []
        for step in self.steps:
            if step[0] == 0 and step[1] == 0:
                continue
            adjacent_cell = (a+step[0], b+step[1])
            if adjacent_cell[0] not in range(1, 11) or adjacent_cell[1] not in range(1, 11):
                continue
            if adjacent_cell in self.used_cells:
                continue
            adjacent.append(adjacent_cell)
            self.used_cells.append(adjacent_cell)
        return adjacent

    def conquer(self, animal: str = None, cell: tuple[int] = None) -> 'Safari':
        if not cell:
            cell = self.get_random_cell()
            animal = self.field[cell[0]-1][cell[1]-1]
        if animal == 'D':
            return self
        for cell in self.get_adjacent_cells(cell):
            animal_in_cell = self.field[cell[0]-1][cell[1]-1]
            if self.animals.index(animal_in_cell) < self.animals.index(animal):
                self.field[cell[0]-1][cell[1]-1] = '-'
                self.conquer(animal=animal, cell=cell)
        return self

    def __repr__(self) -> str:
        repr = ''
        for row in self.field:
            for cell in row:
                repr += cell + ' '
            repr += '\n'
        return repr


test = [['T', 'L', 'L', 'W', 'T', 'L', 'W', 'L', 'D', 'L'],
        ['T', 'W', 'T', 'D', 'D', 'D', 'D', 'L', 'L', 'T'],
        ['W', 'L', 'T', 'D', 'D', 'W', 'T', 'T', 'D', 'L'],
        ['W', 'D', 'T', 'D', 'W', 'D', 'L', 'D', 'T', 'L'],
        ['W', 'L', 'D', 'W', 'D', 'W', 'W', 'W', 'D', 'W'],
        ['D', 'D', 'D', 'W', 'T', 'W', 'W', 'L', 'W', 'W'],
        ['W', 'L', 'W', 'D', 'T', 'W', 'L', 'L', 'D', 'D'],
        ['T', 'W', 'D', 'W', 'W', 'L', 'W', 'W', 'W', 'T'],
        ['D', 'W', 'T', 'T', 'T', 'T', 'W', 'T', 'T', 'D'],
        ['L', 'L', 'D', 'T', 'L', 'D', 'W', 'D', 'T', 'W']]
a = Safari()
a.field = test
print(a.conquer(cell=(9, 9), animal='T'))
# print(a.conquer())
