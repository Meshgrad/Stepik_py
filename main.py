

def sourcetemplate(query_string):
    def ld(**kwargs):
        nonlocal query_string
        if len(kwargs) == 0:
            return query_string
        else:
            query_string += '?'
            for key, value in sorted(kwargs.items()):
                query_string+= f"&{key}={value}"
        return query_string
    return ld

url = 'https://all_for_comfort_life.com'
load = sourcetemplate(url)
print(load(smartphone='iPhone', notebook='huawei', sale=True))