

def create_dict(keys1, values1):
    diction1 = {}
    i = 0
    if len(keys1) > len(values1):
        for key in keys1:
            i = keys.index(key)
            if i < len(values1):
                diction1[key] = values1[i]
            else:
                diction1[key] = None
        return diction1
    else:
        while True:
            i = 0
            for key in keys:
                diction1[key] = values[i]
                i += 1
            break
        return diction1


keys = ['a', 'b', 'c', 'd']
# values = [1, 2, 3, 4, 5, 6]
values = [1, 2, 3]
diction = create_dict(keys, values)
print(diction)
