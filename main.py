
def dict_travel(nested_dicts):
    def rec(nested_dicts, fold=[]):
        if type(nested_dicts) != dict:
            print(f"{'.'.join(fold)}: {nested_dicts}")
        if type(nested_dicts) == dict:
            for k, v in sorted(nested_dicts.items()):
                rec(v, fold + [k])
    rec(nested_dicts, [])
    return

data = {'b': {'c': 30, 'a': 10, 'b': {'d': 40, 'e': 50}}}

dict_travel(data)