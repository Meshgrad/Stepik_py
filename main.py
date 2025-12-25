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
        if len(string) < 9: raise LengthError
        if not (string != string.lower() and string != string.upper() and not (any(x in punctuation for x in string))): raise LetterError
        if not any(i.isdigit() for i in string): raise DigitError
        
    except LengthError:
        raise
    except LetterError:
        raise
    except DigitError:
        raise 
    
    
try:
    print(is_good_password('!@#$%^&*()_+'))
except Exception as err:
    print(type(err))