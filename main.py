

def is_power(number):
    if a == 0 and b == 0:
        return 0
    elif b == 0:
        return 1 + recursive_sum(a - 1, 0)
    else:
        return 1 + recursive_sum(a, b - 1 )


print(recursive_sum(0, 78))