

def hundred(num):
    if num <= 100:
        print(num)
        hundred(num + 1)
hundred(1)

