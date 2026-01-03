

def is_greater(lists, number):
    return any([x > number for x in list(map(sum, lists))])
data = [[0, 0, 1], [0, 1, 0], [1, 0, 0]]

print(is_greater(data, 2))