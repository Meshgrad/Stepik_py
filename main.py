

def recurs(num):
    res = 0
    if len(num) == 1:
        return 1
    else:
        return 1 + recurs(num[1:])
    
print(recurs(input()))