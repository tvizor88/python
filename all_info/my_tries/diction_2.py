diction = {}
keys = ['a', 'b', 'c', 'd']
# values = [1, 2, 3, 4, 5, 6]
values = [1, 2, 3]
if len(keys) > len(values):
    for key in keys:
        i = keys.index(key)
        if i < len(values):
            diction[key] = values[i]
        else:
            diction[key] = None
else:
    while True:
        i = 0
        for key in keys:
            diction[key] = values[i]
            i += 1
        break
print(diction)
