def to_binary(number):
    if int(number) == 0:
        return 0
    elif int(number) == 1:
        return 1
    else:
        return str(to_binary((number) // 2)) + str(int(number) % 2)
        