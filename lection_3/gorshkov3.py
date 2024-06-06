import string
import secrets
import csv
import json
"""
1. There are two lists, possibly of different lengths.
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
"""
first solution
"""


print("task 1 dictionary from 2 lists____done")
print('task one first option without function')
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


"""
second solution with function
"""


print("task one 2-nd option with function")


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


"""
2. Create a new list of odd numbers that starts at one and ends at fifteen by unpacking a range object
Note: to unpack range to list use the asterisk character (*)
"""


print("task 2 odd numbers________________done")
odd_numbers = [*range(1, 16, 2)]
print(odd_numbers)


"""
3. Create a function which filters input list and returns list of integer elements from the input
input_list = [1, 2, '3', 4, None, 10, 33, 'Python', -37.5]
Create different solutions:
- using for loop
- using list comprehensions
- using filter() + lambda
"""


print("task 3 numbers from list loop_____done")


def list_filtering(input_list):
    result = []
    for element in input_list:
        try:
            if int(element) == element:
                result.append(element)
        except (ValueError, TypeError):
            print("wrong value type")
    print("input list", input_list)
    return result


elements = [1, 2, '3', 4, None, 10, 33, 'Python', -37.5]
filtered_elements = list_filtering(elements)
print("output list", filtered_elements)


print("task 3 list comprehensions____________")

print("task 3 filter() + lambda______________")
"""
4. Generate a random Password which meets the following conditions:
Password length must be 10 characters long.
It must contain at least 2 upper case letters, 1 digit, and 1 special symbol.
"""


print("task 4 code generator_____________done")
alphabet = string.ascii_letters + string.digits + string.punctuation
while True:
    password = ''.join(secrets.choice(alphabet) for i in range(10))
    if (sum(c.isupper() for c in password) >= 2
            and sum(c.isdigit() for c in password) >= 1
            and sum(not c.isalnum() for c in password) >= 1):
        print(password)
        break


"""
5. Read cars.csv file, convert its content into json format and write it into cars.json file.
Notes: 
1) use csv.DictReader
2) use json.dump with parameter indent=2
"""


print("task 5 preparing JSON from CSV____done")


csv_file_path = 'D:\python\project\python\lection_3\cars.csv'
json_list = []


with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        json_list.append(row)


with open('output.json', mode='w', encoding='utf-8') as jsonfile:
    json.dump(json_list, jsonfile, ensure_ascii=False, indent=2)

print("check 'output.json' file")

"""
6. Write a primitive calculator. User input is assumed to be a formula (in string format) 
that consist of a number, an operator (+, -, *, /), 
and another number, separated by whitespace (e.g. 1 + 1). Split input string into list,
and check whether the resulting list is valid:
If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.
Try to convert the first and third element to a float. Catch any ValueError that occurs, 
and raise a FormulaError instead
If the second element is not one of operators, again raise a FormulaError
If the input is valid, perform the calculation and print out the result.
"""


print("task 6 calculator         ____________")


"""
7. Write a function that takes in a positive parameter num and returns its multiplicative persistence, 
which is the number of times you must multiply the digits in num until you reach a single digit.
39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
4 --> 0 (because 4 is already a one-digit number)
"""


print("task 7 iterator till one symbol___done")


def iterator():
    while True:
        try:
            print("enter any positive number or print EXIT")
            operation = input()
            count = 0
            if operation == "exit":
                break
            elif operation.isdigit():
                # print("number is correct")
                length_of_number = len(operation)
                print("length", length_of_number)
                while length_of_number > 1:
                    operation = str(sum(map(int, operation)))
                    print(operation)
                    count += 1
                    length_of_number = len(operation)
                print("iteration count =", count)
        except Exception:
            print("inputted value is not a number")


iterator()


"""
8. Implement custom @timeit decorator
Notes:
- use functools.wraps
- use round() to round time to milliseconds. round(0.6666666, 3) -> 0.667
"""
print("task 8 decorator______________________")
