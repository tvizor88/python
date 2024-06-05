"""
Create a function which filters input list and returns list of integer elements from the input
input_list = [1, 2, '3', 4, None, 10, 33, 'Python', -37.5]
Create different solutions:
- using for loop
- using list comprehensions
- using filter() + lambda
"""


def filter_elements(elements_to_filter):
    result = []
    for element in elements_to_filter:
        try:
            if int(element) == element:
                result.append(element)
        except (ValueError, TypeError):
            print("wrong value type")
    print(elements_to_filter)
    return result


elements = [1, 2, '3', 4, None, 10, 33, 'Python', -37.5]
filtered_elements = filter_elements(elements)
print(filtered_elements)
