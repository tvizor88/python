def filter_integers(input_list):
    return [x for x in input_list if isinstance(x, int)]
input_list = [1, 2, '3', 4, None, 10, 33, 'Python', -37.5]
filtered_list = filter_integers(input_list)
print(filtered_list)
