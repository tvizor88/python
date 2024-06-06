def add_space(s):
    new_str = ''
    for char in s:
        if char.isupper():
            new_str += ' ' + char
        else:
            new_str += char
    return new_str

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