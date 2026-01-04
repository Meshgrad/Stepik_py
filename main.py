

def custom_isinstance(objects, typeinfo):
    count  = 0
    for i in objects:
        if isinstance(i, typeinfo):
            count += 1
    return count

numbers = [1, 'two', 3.0, 'четыре', 5, 6.0]
print(custom_isinstance(numbers, (int, float)))
