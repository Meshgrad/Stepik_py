from string import punctuation
class PasswordError(Exception):
    pass

class LengthError(PasswordError):
    pass

class LetterError(PasswordError):
    pass

class DigitError(PasswordError):
    pass

def is_good_password(string):
    try:
        string[8]
    except IndexError:
        raise LengthError

    try:
        list(filter(str.isupper, string))[0]
        list(filter(str.islower, string))[0]
    except IndexError:
        raise LetterError

    try:
        list(filter(str.isdigit, string))[0]
    except IndexError:
        raise DigitError

    return True

while True:
    try:
        is_good_password(input())
    except Exception as err:
        print(err.__class__.__name__)
    else:
        print("Success!")
        break

