def rem_el(element, array):
    arr = []
    for number in array:
        if number != element:
            arr += [number]
    return arr


print(rem_el(1, [1, 1, 2, 3, 4, 5, 1, 21, 2]))
