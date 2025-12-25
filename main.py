import string


def is_good_password(string):
    if not (len(string) >= 9):
        return False
    if not any(i.is_digit() for i in string):
           return False
    if not (string != string.lower() and string != string.upper()):
        return False
    return True
              