
def get_value(nested_dicts, key):
    if key in nested_dicts:
        return nested_dicts[key]                # базовый случай
    
    for v in nested_dicts.values():
        if type(v) == dict:
            value = get_value(v, key)    # рекурсивный случай
            if value is not None:
                return value 
    
            
data = {'first_name': 'Alyson', 'last_name': 'Hannigan', 'birthday': {'day': 24, 'month': 'March', 'year': 1974}}

print(get_value(data, 'birthday'))
    