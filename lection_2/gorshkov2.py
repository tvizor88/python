"""
Print the number of times that the string "hi" appears anywhere in the given string.
'abc hi ho' -> 1
'ABChi hi' -> 2
'hihi' -> 2
"""

from collections import Counter  # import counter
import re  # import module to work with patterns


def count_hi(times):  # declarate the function
    return times.count('hi')  # declarate what should be counted


print(count_hi('abc hi ho'))  # work with string
print(count_hi('ABChi hi'))  # work with string
print(count_hi('hihi'))  # work with string
print('______________________')  # separate tasks results
"""
Print the number of even ints in the given list. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
[2, 1, 2, 3, 4] -> 3
[2, 2, 0] -> 3
[1, 3, 5] -> 0
"""


def count_even_numbers(nums):  # declarate the function
    return sum(1 for num in nums if num % 2 == 0)  # describing the formula


print(count_even_numbers([2, 1, 2, 3, 4]))  # print the result
print(count_even_numbers([2, 2, 0]))  # print the result
print(count_even_numbers([1, 3, 5]))  # print the result
print('______________________')  # separate tasks results

"""
Remove all the occurrences of an element from a list and print resulting list
1, [1, 1, 2, 3, 4, 5, 1, 2] -> [2, 3, 4, 5, 2]
7, [5, 6, 7, 8, 9, 10, 7] -> [5, 6, 8, 9, 10]
4, [1, 2, 3] -> [1, 2, 3]
"""


def remove_element(element, array):  # declarate the function
    return [number for number in array if number != element]  # describing the formula excepting search element


print(remove_element(1, [1, 1, 2, 3, 4, 5, 1, 2]))  # print reformated array
print(remove_element(7, [5, 6, 7, 8, 9, 10, 7]))  # print reformated array
print(remove_element(4, [1, 2, 3]))  # print reformated array
print('______________________')  # separate tasks results

"""
Given list of Strings, your task is to add a space before sequence which 
begins with capital letters to make separate words.
['everyOne', 'lovesPython', 'becauseItIsEasy'] -> ['every One', 'loves Python', 'because It Is Easy']
['LoremIpsumDolorSitAmet'] -> [‘Lorem Ipsum Dolor Sit Amet’]
['onlysmall', 'lettershere'] -> ['onlysmall', 'lettershere']
"""


def add_space(s):  # declarate the function
    return re.sub(r'(?=[A-Z])', ' ', s)  # declarate pattern that search Upper letter


strings = ['everyOne', 'lovesPython', 'becauseItIsEasy',
           'LoremIpsumDolorSitAmet', 'onlysmall', 'lettershere']  # input string
formatted_strings = [add_space(s) for s in strings]  # creating reformated string + spaces
print(formatted_strings)  # printing output string
print('______________________')  # separate tasks results

"""
Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, 
or whatever is there if the string is less than length 3. 
Print n copies of the front
'Chocolate', 2 -> 'ChoCho'
'Chocolate', 3 -> 'ChoChoCho'
'Ab', 3 -> 'AbAbAb'
"""


def repeater(cut, n):  # function declaration
    word = cut[:3]  # cut first 3 letters
    return word * n  # duplicate cut letters


print(repeater('Chocolate', 2))  # print result
print(repeater('Chocolate', 3))  # print result
print(repeater('Ab', 3))  # print result
print('______________________')  # separate tasks results

"""
Given a list of ints, return True if one of the last 4 elements in the list is a 9. 
The list length may be less than 4.
[1, 2, 9, 3, 4] -> True
[9, 1, 2, 3, 4] -> False
[1, 2, 3] -> False
"""


def check_nine(nums):  # declarate function
    return 9 in nums[-4:]  # search if nine appears in 4 last positions


print(check_nine([1, 2, 9, 3, 4]))  # print result
print(check_nine([9, 1, 2, 3, 4]))  # print result
print(check_nine([1, 2, 3]))  # print result
print('______________________')  # separate tasks results

"""
The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. 
In this example, the "i" tag makes <i> and </i> which surround the word "Yay". 
Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".
'i', 'Yay' -> '<i>Yay</i>'
'i', 'Hello' -> '<i>Hello</i>'
'cite', 'Yay' -> '<cite>Yay</cite>'
"""


def html(tag, word):  # declarate function
    return f'<{tag}>{word}</{tag}>'  # declarate output pattern


print(html('i', 'Yay'))  # work with string and tag
print(html('i', 'Hello'))  # work with string and tag
print(html('cite', 'Yay'))  # work with string and tag
print('______________________')  # separate tasks results

"""
Return the "centered" average of an array of ints, which we'll say is the mean average of the values, 
except ignoring the largest and smallest values in the array. 
If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. 
Use int division to produce the final average. You may assume that the array is length 3 or more.
[1, 2, 3, 4, 100] → 3
[1, 1, 5, 5, 10, 8, 7] -> 5
[-10, -4, -2, -4, -2, 0] -> -3
"""


def centered_average(nums):  # declaration the function
    nums.sort()  # sort the array
    trimmed_nums = nums[1:-1]  # remove the smallest and largest
    total = sum(trimmed_nums)  # summ of array elements
    count = len(trimmed_nums)  # check length of array
    return total // count  # calculating the average


print(centered_average([1, 2, 3, 4, 100]))  # print reworked array according function logic
print(centered_average([1, 1, 5, 5, 10, 8, 7]))  # print reworked array according function logic
print(centered_average([-10, -4, -2, -4, -2, 0]))  # print reworked array according function logic
print('______________________')  # separate tasks results

"""
Remove all duplicates from a given string
Input : "Hello world!"
Output : "Helo wrd!"
"""


def remove_duplicates(input_string):  # function declaration
    result = ""  # set empty string for result collection
    seen = set()  # variable for unic symbols
    for char in input_string:  # starting the loop checking letter by letter
        if char not in seen:  # check if letter was already met
            seen.add(char)  # add char to seen after it met
            result += char  # add char to output string
    return result  # output string


input_str = "Hello world!"  # string to work with
output_str = remove_duplicates(input_str)  # output string according no duplicate logic
print(output_str)  # print output string
print('______________________')  # separate tasks results

"""
Find a character with maximal frequency in given String and how many times it appears in this String
Note: there may be more than one such character
Input : "Yep, not the easiest task"
Output : [['t', 4], ['e', 4], [' ', 4]]
"""


def find_max_frequency(input_string):  # declarate function
    freq = Counter(input_string)  # create counter object to count each letter
    max_freq = max(freq.values())  # find the max number of counts
    max_freq_chars = [[char, count] for char, count in freq.items() if count == max_freq]
    # creating the list and count of max counted chars
    return max_freq_chars  # return this list


input_str = "Yep, not the easiest task"  # the string to work with
output = find_max_frequency(input_str)  # prepare the list
print(output)  # print the list
