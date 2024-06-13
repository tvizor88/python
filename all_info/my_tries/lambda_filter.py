el = [1, 2, '3', 4, None, 10, 33, 'Python', -37.5]
# is_int = lambda x: type(x) == int
filtered_list = list(filter(lambda x: type(x) is int, el))
#filtered_list = list(filter(is_int, el))
print(filtered_list)
