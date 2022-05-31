import re


adj_rel = (
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1)
)

def annotate(minefield):
    # no rows
    if not minefield:
        return []

    # no columns
    if not minefield[0]:
        return [""]

    num_of_rows = len(minefield)
    num_of_columns = len(minefield[0])
    for row in minefield:
        if re.match('[^*\s]', row) or len(row) != num_of_columns:
            raise ValueError('The board is invalid with current input.')

    nums_matrix = [[0]*num_of_columns for _ in range(num_of_rows)]
    for i, row in enumerate(minefield):
        for j, cell in enumerate(row):
            if cell != '*':
                continue
            for adj in adj_rel:
                a_r, a_c = [sum(x) for x in zip((i, j), adj)]
                if 0 <= a_r < num_of_rows and 0 <= a_c < num_of_columns:
                    if minefield[a_r][a_c] != '*':
                        nums_matrix[a_r][a_c] += 1
    

    for i, row in enumerate(minefield):
        for j, cell in enumerate(row):
            if cell == '*':
                nums_matrix[i][j] = '*'
            elif nums_matrix[i][j] == 0:
                nums_matrix[i][j] = ' '
            else:
                nums_matrix[i][j] = str(nums_matrix[i][j])

    return [''.join(row) for row in nums_matrix]
