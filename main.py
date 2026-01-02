

def convert(number):
    return (format(number, 'b'), '%o' % number, '%X' % number)

print(convert(-24))