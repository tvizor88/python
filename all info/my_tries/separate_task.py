def remove_duplicates(input_string):
    res = ""
    seen = ""
    for char in input_string:
        if char not in seen:
            seen += char
            res += char
    return res


input_str = "Helsloкенеуыееууыеууе world!"  # string to work with
output_str = remove_duplicates(input_str)  # output string according no duplicate logic
print(output_str)  # print output string
print('______________________')  # separate tasks results
