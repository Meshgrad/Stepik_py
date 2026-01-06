

def remove_marks(text:str, marks:str):
    remove_marks.__dict__.setdefault('count', 0)
    remove_marks.count += 1
    
    res = text
    for mark in marks:
        res = res.replace(mark, '')
    return res
    
    
text = 'Hi! Will we go together?'

print(remove_marks(text, '!?'))
print(remove_marks.count)