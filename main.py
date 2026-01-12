

def filterfalse(predicate, iterable):
    if predicate != None:
        return filter(lambda x:  not predicate(x), iterable)
    else:
        return filter(lambda x:  not bool(x), iterable)

numbers = (1, 2, 3, 4, 5)

print(*filterfalse(lambda x: x % 2 == 0, numbers))