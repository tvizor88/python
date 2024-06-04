def add_space(s):
    new_string = ''
    for char in s:
        if char.isupper():
            new_string += ' ' + char
        else:
            new_string += char
    return new_string

strings = [
"everyOne",
"lovesPython",
"becauseItIsEasy",
"LoremIpsumDolorSitAmet",
"onlysmall",
"lettershere",
]

formatted_strings = [add_space(s) for s in strings]

if __name__ == '__main__':
    print(formatted_strings)