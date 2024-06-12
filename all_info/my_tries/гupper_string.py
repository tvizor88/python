def add_space(s):
    new_str = ''
    for char in s:
        if char.isupper():
            new_str += ' ' + char
        else:
            new_str += char
    return new_str.strip()  # Удаляем пробел в начале, если он есть

# Теперь мы вызываем функцию для каждой строки в списке
strings = [
"everyOne",
"lovesPython",
"becauseItIsEasy",
"LoremIpsumDolorSitAmet",
"onlysmall",
"lettershere",
]

# Используем генератор списка для применения функции ко всем строкам
modified_strings = [add_space(s) for s in strings]

# Печатаем результат
print(modified_strings)

