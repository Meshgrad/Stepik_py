

def sorting(string:str):
    a, b, c = [], [], []
    for ch in string:
        if ch == ch.lower() and not ch.isdigit():
            a.append(ch)
        elif ch == ch.upper() and not ch.isdigit():
            b.append(ch)
        elif ch.isdigit():
            c.append(ch)
    return ''.join(sorted(a) + sorted(b) + sorted(c, key=lambda x: (int(x) % 2 == 0, int(x))))
    
    
print(sorting(input()))