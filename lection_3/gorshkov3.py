
"""

There are two lists, possibly of different lengths.
The first one consists of keys, the second one consists of values.
Write a function create_dict(keys, values) that returns a dictionary created from keys and values.
If there are not enough values, the rest of keys should have a None value. If there not enough keys,
just ignore the rest of values.

Example 1
keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3]
create_dict(keys, values) # returns {'a': 1, 'b': 2, 'c': 3, 'd': None}

Example 2:
keys = ['a', 'b', 'c']
values = [1, 2, 3, 4]
create_dict(keys, values) # returns {'a': 1, 'b': 2, 'c': 3}
"""

def create_dict(keys, values):

  pass





"""
Create a new list of odd numbers that starts at one and ends at fifteen by unpacking a range object
Note: to unpack range to list use the asterisk character (*)
"""



# Your code here





"""
Create a function which filters input list and returns list of integer elements from the input
input_list = [1, 2, '3', 4, None, 10, 33, 'Python', -37.5]
Create different solutions:
- using for loop
- using list comprehensions
- using filter() + lambda
"""

def list_filtering(input_list):

  pass



"""
Generate a random Password which meets the following conditions:
Password length must be 10 characters long.
It must contain at least 2 upper case letters, 1 digit, and 1 special symbol.
"""



# Your code here





"""
Read cars.csv file, convert its content into json format and write it into cars.json file.
Notes: 
1) use csv.DictReader
2) use json.dump with parameter indent=2
"""



# Your code here



"""
Write a primitive calculator. User input is assumed to be a formula (in string format) 
that consist of a number, an operator (+, -, *, /), 
and another number, separated by whitespace (e.g. 1 + 1). Split input string into list,
and check whether the resulting list is valid:
If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.
Try to convert the first and third element to a float. Catch any ValueError that occurs, 
and raise a FormulaError instead
If the second element is not one of operators, again raise a FormulaError
If the input is valid, perform the calculation and print out the result.
"""



# Your code here



"""
Write a function that takes in a positive parameter num and returns its multiplicative persistence, 
which is the number of times you must multiply the digits in num until you reach a single digit.
39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
4 --> 0 (because 4 is already a one-digit number)
"""

def persistence(num):

  pass


"""
Implement custom @timeit decorator
Notes:
- use functools.wraps
- use round() to round time to milliseconds. round(0.6666666, 3) -> 0.667
"""

# Your implementation here




