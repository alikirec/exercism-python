class Matrix:
    def __init__(self, matrix_string):
        self.matrix = [
            [int(cell) for cell in row_str.split(' ')]
            for row_str in matrix_string.split('\n')
        ]


    def row(self, index):
        """
        return row with the given index -- starting from 1
        """
        return self.matrix[index - 1]


    def column(self, index):
        """
        return column with the given index -- starting from 1
        """
        return [row[index - 1] for row in self.matrix]
