

def matrix_to_dict(matrix: list[list[int | float]], ) -> dict[int, list[int | float]]:
    return {idx: value for idx, value in enumerate(matrix, 1)}
annotations = matrix_to_dict.__annotations__

print(annotations['return'])