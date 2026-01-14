import copy 
def get_min_max(data):
    try:
        collect = iter(data)
        mn = mx = next(collect)
        for i in collect:
            if i > mx: mx = i
            if i < mn: mn = i
        return mn, mx
    except:
        pass

iterable = iter(range(10))

print(get_min_max(iterable))


