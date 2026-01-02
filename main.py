
def get_all_values(nested_dicts, key):
    total = set()
    def rec(nested_dicts, key):
        if type(nested_dicts) == dict and key in nested_dicts:
            total.add(nested_dicts[key])
        if type(nested_dicts) == dict:
            
            for v in nested_dicts.values():
                value = rec(v, key)
                #total.update(value)
                #return total
    rec(nested_dicts, key)
    return total
    
my_dict = {
           'Arthur': {'hobby': 'videogames', 'drink': 'cacao'}, 
           'Timur': {'hobby': 'math'},
           'Dima': {
                   'hobby': 'CS',
                   'sister':
                       {
                         'name': 'Anna',
                         'hobby': 'TV',
                         'age': 14
                       }
                   }
           }

result = get_all_values(my_dict, 'hobby')
print(*sorted(result))