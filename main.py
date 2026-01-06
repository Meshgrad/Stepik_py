import string

d = {0: 'в пароле нет ни одной буквы',
         1: 'в пароле нет ни одной заглавной буквы',
         2: 'в пароле нет ни одной строчной буквы',
         3: 'в пароле нет ни одной цифры'}

def verification(login, password, success, failure):
    if not any([x in string.ascii_letters for x in password]):
        failure(login, d[0])
        return
    if not any([x in string.ascii_uppercase for x in password]):
        failure(login, d[1])
        return
    if not any([x in string.ascii_lowercase for x in password]):
        failure(login, d[2])
        return
    if not any([x in string.digits for x in password]):
        failure(login, d[3])
        return
    success(login)

def success(login):
    print(f'Здравствуйте, {login}!')


def failure(login, text):
    print(f'{login}, попробуйте снова. Текст ошибки: {text}')


verification('Arthur_Davletov', 'мойпароль123', success, failure)