

try:
    file = open(input(), 'r', encoding='utf-8')
    print(file.read())
except:
    print("Файл не найден")