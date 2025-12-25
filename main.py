

def print_digits(number):
    new_num = str(number)
    print(new_num[-1])
    if len(new_num) > 1:
        print_digits(int(new_num[:-1]))
print_digits(12345)