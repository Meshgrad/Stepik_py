import calendar

months = dict(zip(list(range(1, 13)), list(calendar.month_name)[1:]))

try:
    num = int(input())
    try:
        print(months[num])
    except KeyError:
        print("Введено число из недопустимого диапазона")
except ValueError:
    print("Введено некорректное значение")
